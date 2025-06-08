import sys
from datetime import datetime
from typing import List, Optional
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
    QFormLayout, QLabel, QLineEdit, QDateTimeEdit, QComboBox, QDoubleSpinBox,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QStatusBar,
    QGroupBox, QSpinBox, QListWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDateTime
import qdarktheme
from App.classes import (
    Isletme, Otobus, Sefer, Bilet, Yolcu,
    OtobusDurumuEnum, SeferDurumuEnum, OdemeDurumuEnum, BiletDurumuEnum, CinsiyetEnum
)
from App.utils import setup_table, clear_form_inputs, get_logger

log = get_logger(__name__)


class IsletmeWidget(QWidget):
    """'İşletme' sekmesini temsil eden widget."""

    def __init__(self, isletme: Isletme, main_window: 'MainWindow'):
        super().__init__()
        self.isletme = isletme
        self.main_window = main_window  # Ana pencereye referans
        self.init_ui()
        self.verileri_yukle()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_group = QGroupBox("İşletme Bilgileri")
        form_layout = QFormLayout()

        self.ad_input = QLineEdit()
        self.adres_input = QLineEdit()
        self.vergi_no_input = QLineEdit()
        self.telefon_input = QLineEdit()
        self.email_input = QLineEdit()

        form_layout.addRow("İşletme Adı:", self.ad_input)
        form_layout.addRow("Adres:", self.adres_input)
        form_layout.addRow("Vergi No:", self.vergi_no_input)
        form_layout.addRow("Telefon:", self.telefon_input)
        form_layout.addRow("Email:", self.email_input)
        form_group.setLayout(form_layout)

        button_layout = QHBoxLayout()
        self.kaydet_btn = QPushButton("Bilgileri Güncelle")
        self.kaydet_btn.clicked.connect(self.bilgileri_kaydet)
        button_layout.addWidget(self.kaydet_btn)
        button_layout.addStretch()

        stats_group = QGroupBox("İşletme İstatistikleri")
        stats_layout = QFormLayout()
        self.otobus_sayisi_label = QLabel("0")
        self.sefer_sayisi_label = QLabel("0")
        self.aktif_sefer_label = QLabel("0")
        self.yolcu_sayisi_label = QLabel("0")
        self.bilet_sayisi_label = QLabel("0")
        stats_layout.addRow("Toplam Otobüs:", self.otobus_sayisi_label)
        stats_layout.addRow("Toplam Sefer:", self.sefer_sayisi_label)
        stats_layout.addRow("Aktif Sefer:", self.aktif_sefer_label)
        stats_layout.addRow("Toplam Yolcu:", self.yolcu_sayisi_label)
        stats_layout.addRow("Toplam Bilet:", self.bilet_sayisi_label)
        stats_group.setLayout(stats_layout)

        tab_widget = QTabWidget()
        self.otobus_table_overview = QTableWidget()
        self.yolcu_table_overview = QTableWidget()

        setup_table(self.otobus_table_overview, ["Plaka", "Marka", "Model", "Kapasite", "Durum"])
        setup_table(self.yolcu_table_overview, ["ID", "Ad", "Soyad", "TC No", "Telefon", "Email"])

        tab_widget.addTab(self.otobus_table_overview, "Otobüsler")
        tab_widget.addTab(self.yolcu_table_overview, "Yolcular")

        layout.addWidget(form_group)
        layout.addLayout(button_layout)
        layout.addWidget(stats_group)
        layout.addWidget(tab_widget)

    def verileri_yukle(self):
        log.info("İşletme verileri yükleniyor...")
        self.ad_input.setText(self.isletme.ad)
        self.adres_input.setText(self.isletme.adres)
        self.vergi_no_input.setText(self.isletme.vergi_no)
        self.telefon_input.setText(self.isletme.telefon)
        self.email_input.setText(self.isletme.email)
        self.istatistikleri_guncelle()
        self.tablolari_guncelle()

    def istatistikleri_guncelle(self):
        self.otobus_sayisi_label.setText(str(len(self.isletme.otobusler)))
        self.sefer_sayisi_label.setText(str(len(self.isletme.seferler)))
        aktif_seferler = [s for s in self.isletme.seferler if
                          s.durum in [SeferDurumuEnum.SATISTA, SeferDurumuEnum.YOLDA]]
        self.aktif_sefer_label.setText(str(len(aktif_seferler)))
        self.yolcu_sayisi_label.setText(str(len(self.isletme.yolcular)))
        self.bilet_sayisi_label.setText(str(len(self.isletme.biletler)))

    def tablolari_guncelle(self):
        # Otobüs tablosu
        self.otobus_table_overview.setRowCount(len(self.isletme.otobusler))
        for row, otobus in enumerate(self.isletme.otobusler):
            self.otobus_table_overview.setItem(row, 0, QTableWidgetItem(otobus.plaka))
            self.otobus_table_overview.setItem(row, 1, QTableWidgetItem(otobus.marka))
            self.otobus_table_overview.setItem(row, 2, QTableWidgetItem(otobus.model))
            self.otobus_table_overview.setItem(row, 3, QTableWidgetItem(str(otobus.kapasite)))
            self.otobus_table_overview.setItem(row, 4, QTableWidgetItem(otobus.durum.value))

        # Yolcu tablosu
        self.yolcu_table_overview.setRowCount(len(self.isletme.yolcular))
        for row, yolcu in enumerate(self.isletme.yolcular):
            self.yolcu_table_overview.setItem(row, 0, QTableWidgetItem(str(yolcu.yolcu_id)))
            self.yolcu_table_overview.setItem(row, 1, QTableWidgetItem(yolcu.ad))
            self.yolcu_table_overview.setItem(row, 2, QTableWidgetItem(yolcu.soyad))
            self.yolcu_table_overview.setItem(row, 3, QTableWidgetItem(yolcu.tc_kimlik_no))
            self.yolcu_table_overview.setItem(row, 4, QTableWidgetItem(yolcu.telefon))
            self.yolcu_table_overview.setItem(row, 5, QTableWidgetItem(yolcu.email))

    def bilgileri_kaydet(self):
        try:
            self.isletme.ad = self.ad_input.text().strip()
            self.isletme.adres = self.adres_input.text().strip()
            self.isletme.vergi_no = self.vergi_no_input.text().strip()
            self.isletme.telefon = self.telefon_input.text().strip()
            self.isletme.email = self.email_input.text().strip()
            QMessageBox.information(self, "Başarılı", "İşletme bilgileri güncellendi!")
            self.main_window.setWindowTitle(f"Otobüs Yönetim Sistemi - {self.isletme.ad}")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bilgiler kaydedilemedi: {e}")
            log.error(f"İşletme bilgileri kaydedilemedi: {e}", exc_info=True)


class SeferEkleWidget(QWidget):
    """'Seferler' sekmesini temsil eden widget."""

    def __init__(self, isletme: Isletme, main_window: 'MainWindow'):
        super().__init__()
        self.isletme = isletme
        self.main_window = main_window
        self.init_ui()
        self.populate_otobus_combobox()
        self.tabloyu_guncelle()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_group = QGroupBox("Yeni Sefer Ekle")
        form_layout = QFormLayout()

        self.sefer_kodu_input = QLineEdit()
        self.kalkis_input = QLineEdit()
        self.varis_input = QLineEdit()
        self.kalkis_zamani_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.kalkis_zamani_input.setCalendarPopup(True)
        self.varis_zamani_input = QDateTimeEdit(QDateTime.currentDateTime().addSecs(3600))
        self.varis_zamani_input.setCalendarPopup(True)
        self.guzergah_input = QLineEdit()
        self.otobus_input = QComboBox()
        self.durum_input = QComboBox()
        self.durum_input.addItems([durum.value for durum in SeferDurumuEnum])

        form_layout.addRow("Sefer Kodu:", self.sefer_kodu_input)
        form_layout.addRow("Kalkış Yeri:", self.kalkis_input)
        form_layout.addRow("Varış Yeri:", self.varis_input)
        form_layout.addRow("Kalkış Zamanı:", self.kalkis_zamani_input)
        form_layout.addRow("Varış Zamanı:", self.varis_zamani_input)
        form_layout.addRow("Güzergah (virgülle ayırın):", self.guzergah_input)
        form_layout.addRow("Otobüs:", self.otobus_input)
        form_layout.addRow("Durum:", self.durum_input)
        form_group.setLayout(form_layout)

        self.form_inputs = [
            self.sefer_kodu_input, self.kalkis_input, self.varis_input,
            self.guzergah_input, self.kalkis_zamani_input, self.varis_zamani_input,
            self.otobus_input, self.durum_input
        ]

        save_btn = QPushButton("Sefer Ekle")
        save_btn.clicked.connect(self.sefer_ekle)

        self.sefer_table = QTableWidget()
        headers = ["Kod", "Kalkış", "Varış", "Kalkış Zamanı", "Otobüs", "Kapasite", "Durum"]
        setup_table(self.sefer_table, headers)

        layout.addWidget(form_group)
        layout.addWidget(save_btn, alignment=Qt.AlignRight)
        layout.addWidget(self.sefer_table)

    def populate_otobus_combobox(self):
        self.otobus_input.clear()
        self.otobus_input.addItem("Seçiniz...", None)
        uygun_otobusler = [o for o in self.isletme.otobusler if o.durum == OtobusDurumuEnum.GARAJDA]
        for otobus in uygun_otobusler:
            self.otobus_input.addItem(f"{otobus.plaka} ({otobus.marka})", otobus)
        self.otobus_input.setEnabled(bool(uygun_otobusler))

    def sefer_ekle(self):
        try:
            selected_otobus = self.otobus_input.currentData()
            if selected_otobus is None:
                QMessageBox.warning(self, "Hata", "Lütfen geçerli bir otobüs seçin.")
                return

            sefer_kodu = self.sefer_kodu_input.text().strip()
            if not sefer_kodu or any(s.sefer_kodu == sefer_kodu for s in self.isletme.seferler):
                QMessageBox.warning(self, "Hata", "Sefer kodu boş veya zaten mevcut olamaz.")
                return

            yeni_sefer = Sefer(
                sefer_kodu=sefer_kodu,
                kalkis_noktasi=self.kalkis_input.text().strip(),
                varis_noktasi=self.varis_input.text().strip(),
                kalkis_zamani=self.kalkis_zamani_input.dateTime().toPyDateTime(),
                varis_zamani=self.varis_zamani_input.dateTime().toPyDateTime(),
                guzergah=[g.strip() for g in self.guzergah_input.text().split(',') if g.strip()],
                durum=SeferDurumuEnum(self.durum_input.currentText())
            )

            self.isletme.sefer_ekle(yeni_sefer)
            selected_otobus.sefer_ekle(yeni_sefer)
            QMessageBox.information(self, "Başarılı", "Sefer başarıyla eklendi!")
            self.formu_temizle()

            # İlgili diğer tüm widget'ları merkezi referans üzerinden güncelle
            self.main_window.guncellemeleri_yay()

        except (ValueError, Exception) as e:
            QMessageBox.critical(self, "Hata", f"Sefer eklenemedi: {e}")
            log.error(f"Sefer eklenemedi: {e}", exc_info=True)

    def tabloyu_guncelle(self):
        log.info("Sefer tablosu güncelleniyor...")
        self.sefer_table.setRowCount(len(self.isletme.seferler))
        sorted_seferler = sorted(self.isletme.seferler, key=lambda s: s.kalkis_zamani, reverse=True)
        for row, sefer in enumerate(sorted_seferler):
            self.sefer_table.setItem(row, 0, QTableWidgetItem(sefer.sefer_kodu))
            self.sefer_table.setItem(row, 1, QTableWidgetItem(sefer.kalkis_noktasi))
            self.sefer_table.setItem(row, 2, QTableWidgetItem(sefer.varis_noktasi))
            self.sefer_table.setItem(row, 3, QTableWidgetItem(sefer.kalkis_zamani.strftime("%d.%m.%Y %H:%M")))
            self.sefer_table.setItem(row, 4, QTableWidgetItem(sefer.otobus.plaka if sefer.otobus else "Atanmamış"))
            self.sefer_table.setItem(row, 5, QTableWidgetItem(str(sefer.otobus.kapasite) if sefer.otobus else "N/A"))
            self.sefer_table.setItem(row, 6, QTableWidgetItem(sefer.durum.value))

    def formu_temizle(self):
        clear_form_inputs(self.form_inputs)
        self.populate_otobus_combobox()


class OtobusListeWidget(QWidget):
    """'Otobüsler' sekmesini temsil eder."""

    def __init__(self, isletme: Isletme, main_window: 'MainWindow'):
        super().__init__()
        self.isletme = isletme
        self.main_window = main_window
        self.current_otobus_plaka = None
        self.init_ui()
        self.tabloyu_guncelle()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_group = QGroupBox("Otobüs Bilgileri")
        form_layout = QFormLayout()

        self.plaka_input = QLineEdit()
        self.marka_input = QLineEdit()
        self.model_input = QLineEdit()
        self.kapasite_input = QSpinBox()
        self.kapasite_input.setObjectName("kapasite_input")  # Form temizleme için özel isim
        self.kapasite_input.setRange(10, 100)
        self.durum_input = QComboBox()
        self.durum_input.addItems([durum.value for durum in OtobusDurumuEnum])

        self.form_inputs = [
            self.plaka_input, self.marka_input, self.model_input,
            self.kapasite_input, self.durum_input
        ]

        form_layout.addRow("Plaka:", self.plaka_input)
        form_layout.addRow("Marka:", self.marka_input)
        form_layout.addRow("Model:", self.model_input)
        form_layout.addRow("Kapasite:", self.kapasite_input)
        form_layout.addRow("Durum:", self.durum_input)
        form_group.setLayout(form_layout)

        button_layout = QHBoxLayout()
        self.add_update_btn = QPushButton("Otobüs Ekle")
        self.add_update_btn.clicked.connect(self.save_otobus)
        self.delete_btn = QPushButton("Seçili Otobüsü Sil")
        self.delete_btn.clicked.connect(self.delete_otobus)
        self.clear_btn = QPushButton("Formu Temizle")
        self.clear_btn.clicked.connect(self.formu_temizle)
        button_layout.addWidget(self.add_update_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.clear_btn)

        self.table = QTableWidget()
        headers = ["Plaka", "Marka", "Model", "Kapasite", "Durum", "Sefer Sayısı"]
        setup_table(self.table, headers)
        self.table.itemSelectionChanged.connect(self.on_selection_changed)

        layout.addWidget(form_group)
        layout.addLayout(button_layout)
        layout.addWidget(self.table)
        self.update_button_states()

    def update_button_states(self):
        has_selection = bool(self.table.selectedItems()) and self.table.currentRow() >= 0
        self.delete_btn.setEnabled(has_selection)

        if self.current_otobus_plaka:
            self.add_update_btn.setText("Otobüs Güncelle")
            self.plaka_input.setReadOnly(True)
        else:
            self.add_update_btn.setText("Otobüs Ekle")
            self.plaka_input.setReadOnly(False)

    def on_selection_changed(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return

        plaka = self.table.item(selected_row, 0).text()
        otobus = next((o for o in self.isletme.otobusler if o.plaka == plaka), None)
        if otobus:
            self.current_otobus_plaka = otobus.plaka
            self.plaka_input.setText(otobus.plaka)
            self.marka_input.setText(otobus.marka)
            self.model_input.setText(otobus.model)
            self.kapasite_input.setValue(otobus.kapasite)
            self.durum_input.setCurrentText(otobus.durum.value)
        self.update_button_states()

    def save_otobus(self):
        if self.current_otobus_plaka:
            self.update_otobus()
        else:
            self.add_otobus()

    def add_otobus(self):
        try:
            plaka = self.plaka_input.text().strip().upper()
            if not plaka or any(o.plaka == plaka for o in self.isletme.otobusler):
                QMessageBox.warning(self, "Hata", "Plaka boş bırakılamaz veya zaten mevcut.")
                return

            yeni_otobus = Otobus(
                plaka=plaka,
                marka=self.marka_input.text().strip(),
                model=self.model_input.text().strip(),
                kapasite=self.kapasite_input.value()
            )
            yeni_otobus.durum = OtobusDurumuEnum(self.durum_input.currentText())
            self.isletme.otobus_ekle(yeni_otobus)
            self.main_window.guncellemeleri_yay()
            QMessageBox.information(self, "Başarılı", f"'{plaka}' plakalı otobüs eklendi.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Otobüs eklenemedi: {e}")
            log.error(f"Otobüs eklenemedi: {e}", exc_info=True)

    def update_otobus(self):
        try:
            otobus = next((o for o in self.isletme.otobusler if o.plaka == self.current_otobus_plaka), None)
            if otobus:
                otobus.marka = self.marka_input.text().strip()
                otobus.model = self.model_input.text().strip()
                otobus.kapasite = self.kapasite_input.value()
                otobus.durum = OtobusDurumuEnum(self.durum_input.currentText())
                self.main_window.guncellemeleri_yay()
                QMessageBox.information(self, "Başarılı", "Otobüs bilgileri güncellendi!")
            else:
                QMessageBox.critical(self, "Hata", "Güncellenecek otobüs bulunamadı.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Otobüs güncellenemedi: {e}")
            log.error(f"Otobüs güncellenemedi: {e}", exc_info=True)

    def delete_otobus(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Uyarı", "Lütfen silmek için bir otobüs seçin.")
            return

        plaka = self.table.item(selected_row, 0).text()
        otobus_to_delete = next((o for o in self.isletme.otobusler if o.plaka == plaka), None)

        if otobus_to_delete:
            if otobus_to_delete.seferler:
                reply = QMessageBox.warning(self, "Silme Onayı",
                                            f"'{plaka}' plakalı otobüsün atanmış seferleri var. "
                                            "Silmek, bu seferlerdeki atamayı kaldıracaktır. Emin misiniz?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.No: return

            reply = QMessageBox.question(self, "Silme Onayı",
                                         f"'{plaka}' plakalı otobüsü silmek istediğinizden emin misiniz?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.isletme.otobus_sil(otobus_to_delete)
                self.main_window.guncellemeleri_yay()
                QMessageBox.information(self, "Başarılı", "Otobüs silindi.")

    def tabloyu_guncelle(self):
        log.info("Otobüs tablosu güncelleniyor...")
        self.table.setRowCount(len(self.isletme.otobusler))
        for row, otobus in enumerate(self.isletme.otobusler):
            self.table.setItem(row, 0, QTableWidgetItem(otobus.plaka))
            self.table.setItem(row, 1, QTableWidgetItem(otobus.marka))
            self.table.setItem(row, 2, QTableWidgetItem(otobus.model))
            self.table.setItem(row, 3, QTableWidgetItem(str(otobus.kapasite)))
            self.table.setItem(row, 4, QTableWidgetItem(otobus.durum.value))
            self.table.setItem(row, 5, QTableWidgetItem(str(len(otobus.seferler))))

    def formu_temizle(self):
        self.current_otobus_plaka = None
        self.table.clearSelection()
        clear_form_inputs(self.form_inputs)
        self.update_button_states()


class BiletWidget(QWidget):
    """'Biletler' sekmesini temsil eder."""

    def __init__(self, isletme: Isletme, main_window: 'MainWindow'):
        super().__init__()
        self.isletme = isletme
        self.main_window = main_window
        self.init_ui()
        self.tabloyu_guncelle()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_group = QGroupBox("Yeni Bilet Ekle")
        form_layout = QFormLayout()

        self.bilet_no_input = QLineEdit()
        self.pnr_input = QLineEdit()
        self.koltuk_no_input = QSpinBox()
        self.koltuk_no_input.setRange(1, 100)
        self.ucret_input = QDoubleSpinBox()
        self.ucret_input.setPrefix("₺")
        self.yolcu_input = QComboBox()
        self.sefer_input = QComboBox()
        self.odeme_durumu_input = QComboBox()
        self.bilet_durumu_input = QComboBox()
        self.odeme_durumu_input.addItems([durum.value for durum in OdemeDurumuEnum])
        self.bilet_durumu_input.addItems([durum.value for durum in BiletDurumuEnum])

        self.form_inputs = [
            self.bilet_no_input, self.pnr_input, self.koltuk_no_input, self.ucret_input,
            self.yolcu_input, self.sefer_input, self.odeme_durumu_input, self.bilet_durumu_input
        ]

        form_layout.addRow("Bilet No:", self.bilet_no_input)
        form_layout.addRow("PNR Kodu:", self.pnr_input)
        form_layout.addRow("Koltuk No:", self.koltuk_no_input)
        form_layout.addRow("Ücret:", self.ucret_input)
        form_layout.addRow("Yolcu:", self.yolcu_input)
        form_layout.addRow("Sefer:", self.sefer_input)
        form_layout.addRow("Ödeme Durumu:", self.odeme_durumu_input)
        form_layout.addRow("Bilet Durumu:", self.bilet_durumu_input)
        form_group.setLayout(form_layout)

        ekle_btn = QPushButton("Bilet Ekle")
        ekle_btn.clicked.connect(self.bilet_ekle)

        self.table = QTableWidget()
        headers = ["Bilet No", "PNR", "Koltuk", "Ücret", "Yolcu", "Sefer", "Ödeme", "Durum"]
        setup_table(self.table, headers)

        layout.addWidget(form_group)
        layout.addWidget(ekle_btn, alignment=Qt.AlignRight)
        layout.addWidget(self.table)

    def populate_comboboxes(self):
        # Yolcu
        self.yolcu_input.clear()
        self.yolcu_input.addItem("Seçiniz...", None)
        for yolcu in self.isletme.yolcular:
            self.yolcu_input.addItem(f"{yolcu.ad} {yolcu.soyad} ({yolcu.tc_kimlik_no})", yolcu)
        self.yolcu_input.setEnabled(bool(self.isletme.yolcular))

        # Sefer
        self.sefer_input.clear()
        self.sefer_input.addItem("Seçiniz...", None)
        for sefer in self.isletme.seferler:
            if sefer.durum == SeferDurumuEnum.SATISTA:
                self.sefer_input.addItem(f"{sefer.sefer_kodu}: {sefer.kalkis_noktasi}-{sefer.varis_noktasi}", sefer)
        self.sefer_input.setEnabled(bool(self.isletme.seferler))

    def bilet_ekle(self):
        try:
            selected_yolcu = self.yolcu_input.currentData()
            selected_sefer = self.sefer_input.currentData()

            if not selected_yolcu or not selected_sefer:
                QMessageBox.warning(self, "Hata", "Lütfen bir yolcu ve satışta olan bir sefer seçin.")
                return

            yeni_bilet = Bilet(
                bilet_no=self.bilet_no_input.text().strip(),
                pnr_kodu=self.pnr_input.text().strip(),
                koltuk_no=self.koltuk_no_input.value(),
                ucret=self.ucret_input.value(),
                durum=BiletDurumuEnum(self.bilet_durumu_input.currentText())
            )
            yeni_bilet.odeme_durumu = OdemeDurumuEnum(self.odeme_durumu_input.currentText())

            selected_yolcu.bilet_ekle(yeni_bilet)
            selected_sefer.bilet_ekle(yeni_bilet)

            QMessageBox.information(self, "Başarılı", "Bilet başarıyla eklendi!")
            self.formu_temizle()
            self.main_window.guncellemeleri_yay()

        except (ValueError, Exception) as e:
            QMessageBox.critical(self, "Hata", f"Bilet eklenemedi: {e}")
            log.error(f"Bilet eklenemedi: {e}", exc_info=True)

    def tabloyu_guncelle(self):
        log.info("Bilet tablosu güncelleniyor...")
        all_biletler = self.isletme.biletler
        self.table.setRowCount(len(all_biletler))
        for row, bilet in enumerate(all_biletler):
            yolcu_str = f"{bilet.yolcu.ad} {bilet.yolcu.soyad}" if bilet.yolcu else "N/A"
            sefer_str = f"{bilet.sefer.sefer_kodu}" if bilet.sefer else "N/A"
            self.table.setItem(row, 0, QTableWidgetItem(bilet.bilet_no))
            self.table.setItem(row, 1, QTableWidgetItem(bilet.pnr_kodu))
            self.table.setItem(row, 2, QTableWidgetItem(str(bilet.koltuk_no)))
            self.table.setItem(row, 3, QTableWidgetItem(f"₺{bilet.ucret:.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(yolcu_str))
            self.table.setItem(row, 5, QTableWidgetItem(sefer_str))
            self.table.setItem(row, 6, QTableWidgetItem(bilet.odeme_durumu.value))
            self.table.setItem(row, 7, QTableWidgetItem(bilet.durum.value))

    def formu_temizle(self):
        clear_form_inputs(self.form_inputs)


class YolcuWidget(QWidget):
    """'Yolcular' sekmesini temsil eder."""

    def __init__(self, isletme: Isletme, main_window: 'MainWindow'):
        super().__init__()
        self.isletme = isletme
        self.main_window = main_window
        self.current_yolcu_id = None
        self.init_ui()
        self.tabloyu_guncelle()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_group = QGroupBox("Yolcu Bilgileri")
        form_layout = QFormLayout()

        self.yolcu_id_input = QLineEdit()
        self.ad_input = QLineEdit()
        self.soyad_input = QLineEdit()
        self.tc_input = QLineEdit()
        self.telefon_input = QLineEdit()
        self.email_input = QLineEdit()
        self.cinsiyet_input = QComboBox()
        self.cinsiyet_input.addItems([c.value for c in CinsiyetEnum])

        self.form_inputs = [
            self.yolcu_id_input, self.ad_input, self.soyad_input, self.tc_input,
            self.telefon_input, self.email_input, self.cinsiyet_input
        ]

        form_layout.addRow("Yolcu ID:", self.yolcu_id_input)
        form_layout.addRow("Ad:", self.ad_input)
        form_layout.addRow("Soyad:", self.soyad_input)
        form_layout.addRow("TC No:", self.tc_input)
        form_layout.addRow("Telefon:", self.telefon_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Cinsiyet:", self.cinsiyet_input)
        form_group.setLayout(form_layout)

        button_layout = QHBoxLayout()
        self.add_update_btn = QPushButton("Yolcu Ekle")
        self.add_update_btn.clicked.connect(self.save_yolcu)
        self.delete_btn = QPushButton("Seçili Yolcuyu Sil")
        self.delete_btn.clicked.connect(self.delete_yolcu)
        self.clear_btn = QPushButton("Formu Temizle")
        self.clear_btn.clicked.connect(self.formu_temizle)
        button_layout.addWidget(self.add_update_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.clear_btn)

        self.table = QTableWidget()
        headers = ["ID", "Ad", "Soyad", "TC No", "Telefon", "Email", "Cinsiyet"]
        setup_table(self.table, headers)
        self.table.itemSelectionChanged.connect(self.on_selection_changed)

        layout.addWidget(form_group)
        layout.addLayout(button_layout)
        layout.addWidget(self.table)
        self.update_button_states()

    def update_button_states(self):
        has_selection = bool(self.table.selectedItems()) and self.table.currentRow() >= 0
        self.delete_btn.setEnabled(has_selection)
        if self.current_yolcu_id:
            self.add_update_btn.setText("Yolcu Güncelle")
            self.yolcu_id_input.setReadOnly(True)
            self.tc_input.setReadOnly(True)
        else:
            self.add_update_btn.setText("Yolcu Ekle")
            self.yolcu_id_input.setReadOnly(False)
            self.tc_input.setReadOnly(False)

    def on_selection_changed(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return

        yolcu_id = self.table.item(selected_row, 0).text()
        yolcu = next((y for y in self.isletme.yolcular if str(y.yolcu_id) == yolcu_id), None)
        if yolcu:
            self.current_yolcu_id = str(yolcu.yolcu_id)
            self.yolcu_id_input.setText(str(yolcu.yolcu_id))
            self.ad_input.setText(yolcu.ad)
            self.soyad_input.setText(yolcu.soyad)
            self.tc_input.setText(yolcu.tc_kimlik_no)
            self.telefon_input.setText(yolcu.telefon)
            self.email_input.setText(yolcu.email)
            self.cinsiyet_input.setCurrentText(yolcu.cinsiyet.value)
        self.update_button_states()

    def save_yolcu(self):
        if self.current_yolcu_id:
            self.update_yolcu()
        else:
            self.add_yolcu()

    def add_yolcu(self):
        try:
            yolcu_id = self.yolcu_id_input.text().strip()
            tc_no = self.tc_input.text().strip()
            if not yolcu_id or any(y.yolcu_id == yolcu_id for y in self.isletme.yolcular):
                QMessageBox.warning(self, "Hata", "Yolcu ID boş veya zaten mevcut olamaz.")
                return
            if not tc_no or any(y.tc_kimlik_no == tc_no for y in self.isletme.yolcular):
                QMessageBox.warning(self, "Hata", "TC Kimlik No boş veya zaten mevcut olamaz.")
                return

            yeni_yolcu = Yolcu(
                ad=self.ad_input.text().strip(),
                soyad=self.soyad_input.text().strip(),
                tc_kimlik_no=tc_no,
                telefon=self.telefon_input.text().strip(),
                email=self.email_input.text().strip(),
                cinsiyet=CinsiyetEnum(self.cinsiyet_input.currentText()),
                yolcu_id=yolcu_id
            )
            self.isletme.yolcu_ekle(yeni_yolcu)
            self.main_window.guncellemeleri_yay()
            QMessageBox.information(self, "Başarılı", "Yolcu eklendi.")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Yolcu eklenemedi: {e}")
            log.error(f"Yolcu eklenemedi: {e}", exc_info=True)

    def update_yolcu(self):
        yolcu = next((y for y in self.isletme.yolcular if str(y.yolcu_id) == self.current_yolcu_id), None)
        if yolcu:
            yolcu.ad = self.ad_input.text().strip()
            yolcu.soyad = self.soyad_input.text().strip()
            yolcu.telefon = self.telefon_input.text().strip()
            yolcu.email = self.email_input.text().strip()
            yolcu.cinsiyet = CinsiyetEnum(self.cinsiyet_input.currentText())
            self.main_window.guncellemeleri_yay()
            QMessageBox.information(self, "Başarılı", "Yolcu güncellendi.")

    def delete_yolcu(self):
        if not self.current_yolcu_id: return
        yolcu = next((y for y in self.isletme.yolcular if str(y.yolcu_id) == self.current_yolcu_id), None)
        if yolcu:
            if yolcu.biletler:
                QMessageBox.warning(self, "Uyarı", "Bu yolcunun biletleri olduğu için silemezsiniz.")
                return
            reply = QMessageBox.question(self, "Silme Onayı",
                                         f"'{yolcu.ad} {yolcu.soyad}' adlı yolcuyu silmek istiyor musunuz?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.isletme.yolcu_sil(yolcu)
                self.main_window.guncellemeleri_yay()
                QMessageBox.information(self, "Başarılı", "Yolcu silindi.")

    def tabloyu_guncelle(self):
        log.info("Yolcu tablosu güncelleniyor...")
        self.table.setRowCount(len(self.isletme.yolcular))
        for row, yolcu in enumerate(self.isletme.yolcular):
            self.table.setItem(row, 0, QTableWidgetItem(str(yolcu.yolcu_id)))
            self.table.setItem(row, 1, QTableWidgetItem(yolcu.ad))
            self.table.setItem(row, 2, QTableWidgetItem(yolcu.soyad))
            self.table.setItem(row, 3, QTableWidgetItem(yolcu.tc_kimlik_no))
            self.table.setItem(row, 4, QTableWidgetItem(yolcu.telefon))
            self.table.setItem(row, 5, QTableWidgetItem(yolcu.email))
            self.table.setItem(row, 6, QTableWidgetItem(yolcu.cinsiyet.value))

    def formu_temizle(self):
        self.current_yolcu_id = None
        self.table.clearSelection()
        clear_form_inputs(self.form_inputs)
        self.update_button_states()


# ==============================================================================
# --- ANA PENCERE VE UYGULAMA BAŞLATMA ---
# ==============================================================================

class CompanySelectionWindow(QMainWindow):
    """Uygulama açılışında firma seçimi/oluşturma ekranı."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Firma Seçimi")
        self.setGeometry(200, 200, 600, 400)
        self.all_companies: List[Isletme] = []
        self.selected_isletme: Optional[Isletme] = None
        self.load_sample_companies()
        self.init_ui()

    def load_sample_companies(self):
        log.info("Örnek veriler oluşturuluyor...")
        isletme1 = Isletme("Kamil Koç", "Ankara, Türkiye", "1112223334", "03121112233", "info@kamilkoc.com")
        otobus1_1 = Otobus("18ABK307", "Mercedes", "Travego", 50)
        otobus1_2 = Otobus("06AS201", "MAN", "Lions Coach", 45)
        otobus1_2.durum = OtobusDurumuEnum.BAKIMDA
        isletme1.otobus_ekle(otobus1_1)
        isletme1.otobus_ekle(otobus1_2)

        yolcu1_1 = Yolcu("Can", "Yılmaz", "12345678901", "5321112233", "can@example.com", CinsiyetEnum.ERKEK, "Y001")
        isletme1.yolcu_ekle(yolcu1_1)

        sefer1_1 = Sefer("KAMILKOC01", "Ankara", "İstanbul", datetime(2025, 6, 10, 9, 0), datetime(2025, 6, 10, 15, 0),
                         ["Bolu", "Sakarya"], SeferDurumuEnum.SATISTA)
        isletme1.sefer_ekle(sefer1_1)
        otobus1_1.sefer_ekle(sefer1_1)

        bilet1_1 = Bilet("B001", "KKPNR001", 10, 300.0, BiletDurumuEnum.SATILDI)
        bilet1_1.odeme_durumu = OdemeDurumuEnum.ODENDI
        yolcu1_1.bilet_ekle(bilet1_1)
        sefer1_1.bilet_ekle(bilet1_1)

        isletme2 = Isletme("Karadeniz Seyahat", "Trabzon, Türkiye", "5554443332", "04629876543", "info@karadeniz.com")
        otobus2_1 = Otobus("67TN207", "Mercedes", "Travego", 30)
        isletme2.otobus_ekle(otobus2_1)

        self.all_companies.extend([isletme1, isletme2])

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        company_group = QGroupBox("Mevcut Firmalar")
        company_layout = QVBoxLayout(company_group)
        self.company_list = QListWidget()
        for company in self.all_companies:
            self.company_list.addItem(company.ad)
        company_layout.addWidget(self.company_list)
        main_layout.addWidget(company_group)

        new_company_group = QGroupBox("Yeni Firma Ekle")
        form_layout = QFormLayout(new_company_group)
        self.new_company_ad_input = QLineEdit()
        self.new_company_adres_input = QLineEdit()
        self.new_company_vergi_no_input = QLineEdit()
        self.new_company_telefon_input = QLineEdit()
        self.new_company_email_input = QLineEdit()
        self.new_company_inputs = [
            self.new_company_ad_input, self.new_company_adres_input, self.new_company_vergi_no_input,
            self.new_company_telefon_input, self.new_company_email_input
        ]
        form_layout.addRow("Firma Adı:", self.new_company_ad_input)
        form_layout.addRow("Adres:", self.new_company_adres_input)
        form_layout.addRow("Vergi No:", self.new_company_vergi_no_input)
        form_layout.addRow("Telefon:", self.new_company_telefon_input)
        form_layout.addRow("Email:", self.new_company_email_input)
        main_layout.addWidget(new_company_group)

        button_layout = QHBoxLayout()
        add_company_btn = QPushButton("Yeni Firma Ekle")
        add_company_btn.clicked.connect(self.add_new_company)
        select_company_btn = QPushButton("Seçili Firmayı Aç")
        select_company_btn.clicked.connect(self.select_company)
        exit_btn = QPushButton("Çıkış")
        exit_btn.clicked.connect(QApplication.instance().quit)
        button_layout.addWidget(add_company_btn)
        button_layout.addWidget(select_company_btn)
        button_layout.addWidget(exit_btn)
        main_layout.addLayout(button_layout)
        self.setCentralWidget(central_widget)

    def add_new_company(self):
        ad = self.new_company_ad_input.text().strip()
        if not ad or not self.new_company_adres_input.text().strip():
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen en azından firma adı ve adresini doldurun.")
            return

        if any(c.ad.lower() == ad.lower() for c in self.all_companies):
            QMessageBox.warning(self, "Hata", "Bu isimde bir firma zaten mevcut.")
            return

        new_isletme = Isletme(
            ad, self.new_company_adres_input.text().strip(),
            self.new_company_vergi_no_input.text().strip(),
            self.new_company_telefon_input.text().strip(),
            self.new_company_email_input.text().strip()
        )
        self.all_companies.append(new_isletme)
        self.company_list.addItem(new_isletme.ad)
        QMessageBox.information(self, "Başarılı", f"'{ad}' firması başarıyla eklendi!")
        clear_form_inputs(self.new_company_inputs)

    def select_company(self):
        selected_items = self.company_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Seçim Hatası", "Lütfen bir firma seçin.")
            return

        company_name = selected_items[0].text()
        self.selected_isletme = next((c for c in self.all_companies if c.ad == company_name), None)

        if self.selected_isletme:
            self.main_window = MainWindow(self.selected_isletme)
            self.main_window.show()
            self.hide()


class MainWindow(QMainWindow):
    """Uygulamanın ana penceresi."""

    def __init__(self, isletme: Isletme):
        super().__init__()
        self.isletme = isletme
        self.setWindowTitle(f"Otobüs Yönetim Sistemi - {self.isletme.ad}")
        self.setGeometry(100, 100, 1200, 800)
        try:
            self.setWindowIcon(QIcon("Assets/bus.png"))
        except Exception:
            log.warning("bus.png ikonu bulunamadı.")

        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()

        # Widget'ları oluştururken ana pencereye referans ver
        self.isletme_widget = IsletmeWidget(self.isletme, self)
        self.sefer_ekle_widget = SeferEkleWidget(self.isletme, self)
        self.otobus_liste_widget = OtobusListeWidget(self.isletme, self)
        self.yolcu_widget = YolcuWidget(self.isletme, self)
        self.bilet_widget = BiletWidget(self.isletme, self)

        self.tabs.addTab(self.isletme_widget, "İşletme")
        self.tabs.addTab(self.sefer_ekle_widget, "Seferler")
        self.tabs.addTab(self.otobus_liste_widget, "Otobüsler")
        self.tabs.addTab(self.yolcu_widget, "Yolcular")
        self.tabs.addTab(self.bilet_widget, "Biletler")

        self.tabs.currentChanged.connect(self.guncellemeleri_yay)

        self.setCentralWidget(self.tabs)
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage(f"{self.isletme.ad} firması ile çalışılıyor.")

    def guncellemeleri_yay(self, index=None):
        """
        Tüm sekmelerdeki verileri ve arayüz elemanlarını en güncel hale getirir.
        Bu fonksiyon, herhangi bir sekmede yapılan değişikliğin diğerlerine
        yansımasını sağlar.
        """
        log.info(f"Tüm sekmeler güncelleniyor (aktif sekme index: {index})...")
        # Combobox'ları ve listeleri güncelle
        self.sefer_ekle_widget.populate_otobus_combobox()
        self.bilet_widget.populate_comboboxes()

        # Tüm tabloları yeniden çiz
        self.isletme_widget.verileri_yukle()
        self.sefer_ekle_widget.tabloyu_guncelle()
        self.otobus_liste_widget.tabloyu_guncelle()
        self.yolcu_widget.tabloyu_guncelle()
        self.bilet_widget.tabloyu_guncelle()

    def closeEvent(self, event):
        """Ana pencere kapatıldığında firma seçme ekranını tekrar gösterir."""
        # Bu fonksiyonun düzgün çalışması için CompanySelectionWindow'da bir referans tutulmalı
        # veya uygulama tamamen kapatılabilir. Şimdilik basitçe bırakıldı.
        QApplication.instance().quit()


def main():
    """Uygulamayı başlatan ana fonksiyon."""
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()

    company_selection_window = CompanySelectionWindow()
    company_selection_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

