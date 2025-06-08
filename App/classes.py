# classes.py
from datetime import datetime
from typing import List, Optional
from enum import Enum
import uuid

# Merkezi loglama fonksiyonunu içe aktar
from utils import get_logger

log = get_logger(__name__)

class OtobusDurumuEnum(Enum):
    GARAJDA = "Garajda"
    SEFERDE = "Seferde"
    BAKIMDA = "Bakımda"
    ARIZALI = "Arızalı"


class SeferDurumuEnum(Enum):
    PLANLANDI = "Planlandı"
    SATISTA = "Satışta"
    AKTARMA = "Aktarma"
    YOLDA = "Yolda"
    TAMAMLANDI = "Tamamlandı"
    IPTAL = "İptal"


class OdemeDurumuEnum(Enum):
    ODENDI = "Ödendi"
    ODENMEDI = "Ödenmedi"
    IADE_EDILDI = "İade Edildi"


class BiletDurumuEnum(Enum):
    REZERVE = "Rezerve"
    SATILDI = "Satıldı"
    IPTAL = "İptal"
    KULLANILDI = "Kullanıldı"
    KULLANILMADI = "Kullanılmadı"


class CinsiyetEnum(Enum):
    ERKEK = "Erkek"
    KADIN = "Kadın"
    BELIRTILMEMIS = "Belirtilmemiş"


# SINIF TANIMLARI
class Isletme:
    def __init__(self, ad: str, adres: str, vergi_no: str, telefon: str, email: str):
        log.debug(f"Isletme objesi oluşturuluyor: {ad}")
        self.isletme_id: uuid.UUID = uuid.uuid4()
        self.ad = ad
        self.adres = adres
        self.vergi_no = vergi_no
        self.telefon = telefon
        self.email = email
        self._otobusler: List['Otobus'] = []
        self._seferler: List['Sefer'] = []
        self._yolcular: List['Yolcu'] = []

    @property
    def otobusler(self) -> List['Otobus']:
        return self._otobusler

    def otobus_ekle(self, otobus: 'Otobus'):
        log.debug(f"Otobüs ekleniyor: {otobus.plaka} -> {self.ad}")
        if otobus not in self._otobusler:
            if otobus.isletme and otobus.isletme != self:
                raise ValueError(f"{otobus.plaka} plakalı otobüs zaten başka bir işletmeye kayıtlı.")
            self._otobusler.append(otobus)
            otobus._isletme = self

    def otobus_sil(self, otobus: 'Otobus'):
        log.debug(f"Otobüs siliniyor: {otobus.plaka} from {self.ad}")
        if otobus in self._otobusler:
            for sefer in list(otobus.seferler):
                sefer._otobus = None
            self._otobusler.remove(otobus)
            otobus._isletme = None

    @property
    def seferler(self) -> List['Sefer']:
        return self._seferler

    def sefer_ekle(self, sefer: 'Sefer'):
        log.debug(f"Sefer ekleniyor: {sefer.sefer_kodu} -> {self.ad}")
        if sefer not in self._seferler:
            if sefer.isletme and sefer.isletme != self:
                raise ValueError(f"{sefer.sefer_kodu} kodlu sefer zaten başka bir işletmeye kayıtlı.")
            self._seferler.append(sefer)
            sefer._isletme = self

    def sefer_sil(self, sefer: 'Sefer'):
        log.debug(f"Sefer siliniyor: {sefer.sefer_kodu} from {self.ad}")
        if sefer in self._seferler:
            for bilet in sefer.biletler:
                bilet.durum = BiletDurumuEnum.IPTAL
                if bilet.yolcu and bilet in bilet.yolcu.biletler:
                    bilet.yolcu.bilet_sil(bilet)
            if sefer.otobus and sefer in sefer.otobus.seferler:
                sefer.otobus.sefer_sil(sefer)
            self._seferler.remove(sefer)
            sefer._isletme = None

    @property
    def yolcular(self) -> List['Yolcu']:
        return self._yolcular

    def yolcu_ekle(self, yolcu: 'Yolcu'):
        log.debug(f"Yolcu ekleniyor: {yolcu.ad} {yolcu.soyad} -> {self.ad}")
        if yolcu not in self._yolcular:
            self._yolcular.append(yolcu)

    def yolcu_sil(self, yolcu: 'Yolcu'):
        log.debug(f"Yolcu siliniyor: {yolcu.ad} {yolcu.soyad} from {self.ad}")
        if yolcu in self._yolcular:
            self._yolcular.remove(yolcu)

    @property
    def biletler(self) -> List['Bilet']:
        tum_biletler = []
        for sefer in self.seferler:
            tum_biletler.extend(sefer.biletler)
        return tum_biletler

    def __str__(self):
        return f"İşletme: {self.ad} (ID: {self.isletme_id})"

    def __repr__(self):
        return f"Isletme(ad='{self.ad}')"


class Otobus:
    def __init__(self, plaka: str, marka: str, model: str, kapasite: int):
        log.debug(f"Otobus objesi oluşturuluyor: {plaka}")
        self.otobus_id: uuid.UUID = uuid.uuid4()
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.kapasite = kapasite
        self.durum = OtobusDurumuEnum.GARAJDA
        self._isletme: Optional['Isletme'] = None
        self._seferler: List['Sefer'] = []

    @property
    def isletme(self) -> Optional['Isletme']:
        return self._isletme

    @property
    def seferler(self) -> List['Sefer']:
        return self._seferler

    def sefer_ekle(self, sefer: 'Sefer'):
        log.debug(f"Sefere otobüs atanıyor: {sefer.sefer_kodu} -> {self.plaka}")
        if sefer not in self._seferler:
            if sefer.otobus and sefer.otobus != self:
                raise ValueError(f"{sefer.sefer_kodu} kodlu sefer zaten başka bir otobüse atanmış.")
            if self.durum not in [OtobusDurumuEnum.GARAJDA, OtobusDurumuEnum.SEFERDE]:
                raise ValueError(f"{self.plaka} plakalı otobüs sefere uygun değil. Durum: {self.durum.value}")

            self._seferler.append(sefer)
            sefer._otobus = self
            if self.isletme and sefer.isletme is None:
                self.isletme.sefer_ekle(sefer)
            elif self.isletme and sefer.isletme != self.isletme:
                raise ValueError("Seferin işletmesi ile otobüsün işletmesi farklı olamaz.")
            elif self.isletme is None and sefer.isletme:
                sefer.isletme.otobus_ekle(self)
            self.durum = OtobusDurumuEnum.SEFERDE

    def sefer_sil(self, sefer: 'Sefer'):
        log.debug(f"Seferden otobüs kaldırılıyor: {sefer.sefer_kodu} from {self.plaka}")
        if sefer in self._seferler:
            self._seferler.remove(sefer)
            sefer._otobus = None
            if not self._seferler and self.durum == OtobusDurumuEnum.SEFERDE:
                self.durum = OtobusDurumuEnum.GARAJDA

    def __str__(self):
        return f"Otobüs: {self.plaka} ({self.marka} {self.model})"

    def __repr__(self):
        return f"Otobus(plaka='{self.plaka}')"


class Sefer:
    def __init__(self, sefer_kodu: str, kalkis_noktasi: str, varis_noktasi: str,
                 kalkis_zamani: datetime, varis_zamani: datetime,
                 guzergah: List[str], durum: SeferDurumuEnum):
        log.debug(f"Sefer objesi oluşturuluyor: {sefer_kodu}")
        self.sefer_id: uuid.UUID = uuid.uuid4()
        self.sefer_kodu = sefer_kodu
        self.kalkis_noktasi = kalkis_noktasi
        self.varis_noktasi = varis_noktasi
        self.kalkis_zamani = kalkis_zamani
        self.varis_zamani = varis_zamani
        self.guzergah = guzergah
        self.durum = durum
        self._isletme: Optional['Isletme'] = None
        self._otobus: Optional['Otobus'] = None
        self._biletler: List['Bilet'] = []

        if varis_zamani <= kalkis_zamani:
            raise ValueError("Varış zamanı, kalkış zamanından sonra olmalıdır.")

    @property
    def isletme(self) -> Optional['Isletme']:
        return self._isletme

    @property
    def otobus(self) -> Optional['Otobus']:
        return self._otobus

    @property
    def biletler(self) -> List['Bilet']:
        return self._biletler

    def bilet_ekle(self, bilet: 'Bilet'):
        log.debug(f"Sefere bilet ekleniyor: {bilet.bilet_no} -> {self.sefer_kodu}")
        if not self.otobus:
            raise ValueError("Bilet eklemek için sefere bir otobüs atanmış olmalıdır.")
        if len(self._biletler) >= self.otobus.kapasite:
            raise ValueError(f"Sefer dolu. Kapasite: {self.otobus.kapasite}.")
        if bilet.koltuk_no <= 0 or bilet.koltuk_no > self.otobus.kapasite:
            raise ValueError(f"Koltuk numarası (1-{self.otobus.kapasite}) aralığında olmalıdır.")
        if any(mevcut.koltuk_no == bilet.koltuk_no and mevcut.durum != BiletDurumuEnum.IPTAL for mevcut in self._biletler):
            raise ValueError(f"{bilet.koltuk_no} numaralı koltuk zaten dolu.")

        if bilet not in self._biletler:
            self._biletler.append(bilet)
            bilet._sefer = self

    def bilet_sil(self, bilet: 'Bilet'):
        log.debug(f"Seferden bilet siliniyor: {bilet.bilet_no} from {self.sefer_kodu}")
        if bilet in self._biletler:
            self._biletler.remove(bilet)
            bilet._sefer = None
            if bilet.yolcu and bilet in bilet.yolcu.biletler:
                bilet.yolcu.bilet_sil(bilet)

    def get_bos_koltuk_sayisi(self) -> int:
        if not self.otobus: return 0
        dolu_koltuk_sayisi = len([b for b in self._biletler if b.durum != BiletDurumuEnum.IPTAL])
        return self.otobus.kapasite - dolu_koltuk_sayisi

    def __str__(self):
        return f"Sefer: {self.sefer_kodu} ({self.kalkis_noktasi} -> {self.varis_noktasi})"

    def __repr__(self):
        return f"Sefer(sefer_kodu='{self.sefer_kodu}')"


class Bilet:
    def __init__(self, bilet_no: str, pnr_kodu: str, koltuk_no: int, ucret: float, durum: BiletDurumuEnum):
        log.debug(f"Bilet objesi oluşturuluyor: {bilet_no}")
        self.bilet_id: uuid.UUID = uuid.uuid4()
        self.bilet_no = bilet_no
        self.pnr_kodu = pnr_kodu
        self.koltuk_no = koltuk_no
        self.ucret = ucret
        self.durum = durum
        self.odeme_durumu = OdemeDurumuEnum.ODENMEDI
        self._sefer: Optional['Sefer'] = None
        self._yolcu: Optional['Yolcu'] = None

    @property
    def sefer(self) -> Optional['Sefer']:
        return self._sefer

    @property
    def yolcu(self) -> Optional['Yolcu']:
        return self._yolcu

    def __str__(self):
        yolcu_ad = f"{self.yolcu.ad} {self.yolcu.soyad}" if self.yolcu else "Bilinmiyor"
        return f"Bilet No: {self.bilet_no}, Koltuk: {self.koltuk_no}, Yolcu: {yolcu_ad}"

    def __repr__(self):
        return f"Bilet(bilet_no='{self.bilet_no}')"


class Yolcu:
    def __init__(self, ad: str, soyad: str, tc_kimlik_no: str, telefon: str, email: str,
                 cinsiyet: CinsiyetEnum, yolcu_id: Optional[str] = None):
        log.debug(f"Yolcu objesi oluşturuluyor: {ad} {soyad}")
        self.yolcu_id: str = yolcu_id if yolcu_id else str(uuid.uuid4())
        self.ad = ad
        self.soyad = soyad
        self.tc_kimlik_no = tc_kimlik_no
        self.telefon = telefon
        self.email = email
        self.cinsiyet = cinsiyet
        self._biletler: List['Bilet'] = []

    @property
    def biletler(self) -> List['Bilet']:
        return self._biletler

    def bilet_ekle(self, bilet: 'Bilet'):
        log.debug(f"Yolcuya bilet ekleniyor: {bilet.bilet_no} -> {self.ad} {self.soyad}")
        if bilet not in self._biletler:
            if bilet.yolcu and bilet.yolcu != self:
                raise ValueError(f"{bilet.bilet_no} numaralı bilet zaten başka bir yolcuya ait.")
            self._biletler.append(bilet)
            bilet._yolcu = self

    def bilet_sil(self, bilet: 'Bilet'):
        log.debug(f"Yolcudan bilet siliniyor: {bilet.bilet_no} from {self.ad} {self.soyad}")
        if bilet in self._biletler:
            self._biletler.remove(bilet)
            bilet._yolcu = None

    def __str__(self):
        return f"Yolcu: {self.ad} {self.soyad} (ID: {self.yolcu_id})"

    def __repr__(self):
        return f"Yolcu(ad='{self.ad}', soyad='{self.soyad}')"
