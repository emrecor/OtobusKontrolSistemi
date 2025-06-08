# utils.py
import logging
from typing import List

from PyQt5.QtWidgets import (
    QWidget, QTableWidget, QHeaderView, QLineEdit, QSpinBox,
    QDoubleSpinBox, QComboBox, QDateTimeEdit
)
from PyQt5.QtCore import QDateTime

# DEBUG modunu buradan açıp kapatabilirsiniz.
# True yaparsanız, sınıflardaki tüm adımlar konsola yazdırılır.
DEBUG_MODE = False

# Proje genelinde kullanılacak loglama nesnesini ayarla
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_logger(name: str) -> logging.Logger:
    """Belirtilen isim için bir logger nesnesi döndürür."""
    return logging.getLogger(name)


def setup_table(table: QTableWidget, headers: List[str]):
    """
    Bir QTableWidget için başlıkları, boyutlandırma modunu ve düzenleme
    tetikleyicilerini ayarlar.
    """
    log = get_logger("setup_table")
    log.debug(f"'{table.objectName()}' adlı tablo {headers} başlıklarıyla ayarlanıyor.")
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setEditTriggers(QTableWidget.NoEditTriggers)
    table.setSelectionBehavior(QTableWidget.SelectRows) # Satır bazlı seçim
    table.setSelectionMode(QTableWidget.SingleSelection) # Tek satır seçimi


def clear_form_inputs(widgets: List[QWidget]):
    """
    Verilen widget listesindeki (QLineEdit, QSpinBox vb.) girdileri
    varsayılan değerlerine sıfırlar.
    """
    log = get_logger("clear_form_inputs")
    log.debug("Form temizleniyor...")
    for widget in widgets:
        if isinstance(widget, QLineEdit):
            widget.clear()
        elif isinstance(widget, QSpinBox):
            # Kapasite gibi alanlar için mantıklı bir varsayılan değer
            if "kapasite" in widget.objectName().lower():
                 widget.setValue(40)
            else:
                 widget.setValue(widget.minimum())
        elif isinstance(widget, QDoubleSpinBox):
            widget.setValue(widget.minimum())
        elif isinstance(widget, QComboBox):
            widget.setCurrentIndex(0)
        elif isinstance(widget, QDateTimeEdit):
            widget.setDateTime(QDateTime.currentDateTime())

