Otobüs Yönetim Sistemi
Bu proje, Python ve PyQt5 kütüphanesi kullanılarak geliştirilmiş, otobüs firmaları için kapsamlı bir masaüstü yönetim uygulamasıdır. Uygulama, işletme, otobüs, sefer, yolcu ve bilet yönetimi gibi kritik operasyonların kolayca takip edilmesini sağlar.

(Not: Bu alana uygulamanızın bir ekran görüntüsünü eklemeniz projenizin daha dikkat çekici olmasını sağlar.)

✨ Temel Özellikler
Çoklu Firma Desteği: Uygulama başlangıcında farklı işletmeler seçilebilir veya yeni işletmeler oluşturulabilir.
İşletme Paneli: İşletme bilgileri (adres, vergi no vb.) güncellenebilir. Toplam otobüs, sefer ve yolcu gibi istatistikler anlık olarak takip edilebilir.
Otobüs Filosu Yönetimi:
Yeni otobüs ekleme, mevcut otobüs bilgilerini (marka, model, kapasite) güncelleme ve silme işlemleri.
Otobüslerin durumunu (Garajda, Seferde, Bakımda vb.) yönetme.
Sefer ve Güzergah Planlama:
Detaylı sefer bilgileri (kalkış-varış noktası, zamanı, güzergah) ile yeni seferler oluşturma.
Seferlere uygun durumdaki otobüsleri atama.
Yolcu Yönetimi:
Yolcuların kişisel bilgilerini (TC Kimlik No, iletişim bilgileri) kaydetme, güncelleme ve silme.
Bilet Satış ve Yönetimi:
Mevcut seferler için yolculara bilet kesme.
Bilet detaylarını (koltuk no, ücret, PNR kodu, ödeme durumu) yönetme.
Modern ve Kullanıcı Dostu Arayüz:
Sekmeli yapı sayesinde modüller arası kolay geçiş.
qdarktheme kütüphanesi ile şık bir karanlık tema desteği.
🛠️ Kullanılan Teknolojiler
Python 3: Ana programlama dili.
PyQt5: Masaüstü uygulaması arayüzü için kullanılan kütüphane.
qdarktheme: Modern bir karanlık tema sağlamak için kullanılan kütüphane.
🚀 Kurulum ve Çalıştırma
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

Ön Gereksinimler
Python 3.8+
Git
Adım Adım Kurulum
Projeyi Klonlayın

Bash

git clone https://github.com/emrecor/OtobusKontrolSistemi.git
cd OtobusKontrolSistemi
Sanal Ortam Oluşturun ve Aktif Edin (Önerilir)

Bash

# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
Gerekli Kütüphaneleri Yükleyin
Proje ana dizininde aşağıdaki komutu çalıştırarak requirements.txt dosyasındaki tüm bağımlılıkları yükleyin.

Bash

pip install -r requirements.txt
Eğer requirements.txt dosyanız yoksa, aşağıdaki komutla gerekli kütüphaneleri manuel olarak yükleyebilirsiniz:

Bash

pip install PyQt5 qdarktheme
Uygulamayı Çalıştırın

Bash

python main.py
...
📂 Proje Yapısı
Proje, nesne yönelimli programlama (OOP) prensiplerine uygun olarak modüler bir yapıda tasarlanmıştır.

OtobusKontrolSistemi/
├── .venv/                  # Sanal ortam klasörü
├── app/
│   ├── assets/
│   │   └── bus.png         # Uygulama ikonu
│   ├── __init__.py
│   ├── classes.py          # Ana sınıfların tanımı (Isletme, Otobus, Sefer vb.)
│   ├── main.py             # PyQt5 arayüzü ve ana uygulama mantığı
│   └── utils.py            # Yardımcı fonksiyonlar (loglama, tablo ayarları)
│
├── .gitignore              # Git tarafından takip edilmeyecek dosyalar
├── requirements.txt        # Proje bağımlılıkları
└── README.md               # Proje tanıtım dosyası
🤝 Katkıda Bulunma
Katkılarınız projeyi daha iyi hale getirecektir! Lütfen bir "pull request" açmaktan veya "issue" oluşturmaktan çekinmeyin.

Projeyi "Fork" edin.
Yeni bir "Branch" oluşturun (git checkout -b ozellik/YeniOzellik).
Değişikliklerinizi "Commit" edin (git commit -m 'Yeni bir özellik eklendi').
Oluşturduğunuz "Branch"i "Push" edin (git push origin ozellik/YeniOzellik).
Bir "Pull Request" açın.
