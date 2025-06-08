# 🚌 Otobüs Yönetim Sistemi

Bu proje, Python ve PyQt5 kütüphanesi kullanılarak geliştirilmiş, otobüs firmaları için kapsamlı bir masaüstü yönetim uygulamasıdır. Uygulama, işletme, otobüs, sefer, yolcu ve bilet yönetimi gibi kritik operasyonların kolayca takip edilmesini sağlar.

## ✨ Temel Özellikler

-   **Çoklu Firma Desteği**: Uygulama başlangıcında farklı işletmeler seçilebilir veya yeni işletmeler oluşturulabilir.
-   **İşletme Paneli**: İşletme bilgileri (adres, vergi no vb.) güncellenebilir. Toplam otobüs, sefer ve yolcu gibi istatistikler anlık olarak takip edilebilir.
-   **Otobüs Filosu Yönetimi**:
    -   Yeni otobüs ekleme, mevcut otobüs bilgilerini (marka, model, kapasite) güncelleme ve silme işlemleri.
    -   Otobüslerin durumunu (Garajda, Seferde, Bakımda vb.) yönetme.
-   **Sefer ve Güzergah Planlama**:
    -   Detaylı sefer bilgileri (kalkış-varış noktası, zamanı, güzergah) ile yeni seferler oluşturma.
    -   Seferlere uygun durumdaki otobüsleri atama.
-   **Yolcu Yönetimi**:
    -   Yolcuların kişisel bilgilerini (TC Kimlik No, iletişim bilgileri) kaydetme, güncelleme ve silme.
-   **Bilet Satış ve Yönetimi**:
    -   Mevcut seferler için yolculara bilet kesme.
    -   Bilet detaylarını (koltuk no, ücret, PNR kodu, ödeme durumu) yönetme.
-   **Modern ve Kullanıcı Dostu Arayüz**:
    -   Sekmeli yapı sayesinde modüller arası kolay geçiş.
    -   `qdarktheme` kütüphanesi ile şık bir karanlık tema desteği.

## 🛠️ Kullanılan Teknolojiler

-   **Python 3**: Ana programlama dili.
-   **PyQt5**: Masaüstü uygulaması arayüzü için kullanılan kütüphane.
-   **qdarktheme**: Modern bir karanlık tema sağlamak için kullanılan kütüphane.

## 🚀 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Ön Gereksinimler

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### Adım Adım Kurulum

1.  **Projeyi Klonlayın**
    ```bash
    git clone [https://github.com/emrecor/OtobusKontrolSistemi.git](https://github.com/emrecor/OtobusKontrolSistemi.git)
    cd OtobusKontrolSistemi
    ```

2.  **Sanal Ortam Oluşturun ve Aktif Edin** (Önerilir)
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin**
    Proje ana dizininde aşağıdaki komutu çalıştırarak `requirements.txt` dosyasındaki tüm bağımlılıkları yükleyin.
    ```bash
    pip install -r requirements.txt
    ```
    *Eğer `requirements.txt` dosyanız yoksa, aşağıdaki komutla gerekli kütüphaneleri manuel olarak yükleyebilirsiniz:*
    ```bash
    pip install PyQt5 qdarktheme
    ```

4.  **Uygulamayı Çalıştırın**
    ```bash
    python main.py
    ```

## **📂 Proje Yapısı**



Proje, nesne yönelimli programlama (OOP) prensiplerine uygun olarak modüler bir yapıda tasarlanmıştır.


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



## **🤝 Katkıda Bulunma**



Katkılarınız projeyi daha iyi hale getirecektir! Lütfen bir "pull request" açmaktan veya "issue" oluşturmaktan çekinmeyin.

1.  Projeyi **Fork** edin.
2.  Yeni bir **Branch** oluşturun (`git checkout -b ozellik/YeniOzellik`).
3.  Değişikliklerinizi **Commit** edin (`git commit -m 'Yeni bir özellik eklendi'`).
4.  Oluşturduğunuz **Branch**'i **Push** edin (`git push origin ozellik/YeniOzellik`).
5.  Bir **Pull Request** açın.

## 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.