````markdown
# 🚌 Otobüs Yönetim Sistemi

Bu proje, **Python** ve **PyQt5** kullanılarak geliştirilmiş, otobüs firmalarının operasyonel süreçlerini dijital ortamda kolayca yönetmesini sağlayan masaüstü uygulamasıdır. Uygulama, işletme, otobüs, sefer, yolcu ve bilet işlemlerini kapsayan kapsamlı bir kontrol paneli sunar.

---

## ✨ Özellikler

- **🔹 Çoklu Firma Desteği**  
  Farklı işletmeler arasında geçiş yapılabilir, yeni işletmeler sisteme kolayca eklenebilir.

- **🏢 İşletme Yönetimi**  
  - Firma bilgileri (adres, vergi numarası vb.) güncellenebilir.  
  - Otobüs, sefer ve yolcu istatistikleri anlık görüntülenebilir.

- **🚌 Otobüs Filosu Yönetimi**  
  - Yeni otobüs ekleme, düzenleme ve silme işlemleri.  
  - Durum takibi (Garajda, Seferde, Bakımda).

- **📍 Sefer ve Güzergah Planlama**  
  - Kalkış/varış noktaları ve saatleriyle detaylı sefer planlama.  
  - Müsait otobüslerin seferlere atanması.

- **🧍‍♂️ Yolcu Yönetimi**  
  - Yolcu bilgilerini (TC Kimlik No, iletişim) kaydetme, düzenleme, silme.

- **🎫 Bilet Satış ve Takibi**  
  - Seferlere özel bilet kesimi.  
  - Koltuk no, ücret, PNR kodu ve ödeme durumu takibi.

- **🖥️ Modern Arayüz**  
  - Sekmeli tasarım ile modüller arası hızlı geçiş.  
  - `qdarktheme` ile şık ve modern karanlık tema desteği.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji     | Açıklama                              |
|---------------|----------------------------------------|
| Python 3      | Ana programlama dili                   |
| PyQt5         | GUI (grafik kullanıcı arayüzü) için    |
| qdarktheme    | Karanlık tema desteği                  |

---

## 🚀 Kurulum Talimatları

### Ön Gereksinimler

- Python 3.8+  
- Git

### Kurulum Adımları

1. **Projeyi Klonlayın**

```bash
git clone https://github.com/emrecor/OtobusKontrolSistemi.git
cd OtobusKontrolSistemi
````

2. **Sanal Ortam Oluşturun (Önerilir)**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Bağımlılıkları Yükleyin**

```bash
pip install -r requirements.txt
```

> Eğer `requirements.txt` mevcut değilse:

```bash
pip install PyQt5 qdarktheme
```

4. **Uygulamayı Başlatın**

```bash
python app/main.py
```

---

## 📁 Proje Yapısı

```
OtobusKontrolSistemi/
├── .venv/               # Sanal ortam (opsiyonel)
├── app/
│   ├── assets/          # Görseller, ikonlar
│   │   └── bus.png
│   ├── __init__.py
│   ├── classes.py       # Ana sınıflar (Isletme, Otobus, Sefer vb.)
│   ├── main.py          # Arayüz ve kontrol akışı
│   └── utils.py         # Yardımcı fonksiyonlar
├── requirements.txt     # Bağımlılıklar
├── .gitignore
└── README.md            # Tanıtım dosyası
```

---

## 🤝 Katkı Sağlama

Katkılarınızı memnuniyetle kabul ederiz. Yeni özellikler eklemek veya hata düzeltmeleri yapmak için aşağıdaki adımları izleyin:

1. Projeyi **Fork** edin.
2. Yeni bir **Branch** oluşturun: `git checkout -b ozellik/YeniOzellik`
3. Değişiklikleri **Commit** edin: `git commit -m 'Yeni özellik eklendi'`
4. Branch’i **Push** edin: `git push origin ozellik/YeniOzellik`
5. Bir **Pull Request** açın.

---

## 📝 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

```

Bu içeriği doğrudan `README.md` dosyana yapıştırabilirsin. Dosyayı VS Code veya başka bir metin editörü ile `.md` olarak kaydettiğinde biçimlendirme düzgün görünecektir. Yardımcı olmamı istersen, `.md` dosyasını doğrudan oluşturup sana da sağlayabilirim.
```
