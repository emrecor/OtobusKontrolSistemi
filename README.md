<div align="center">
  <a href="#-otobüs-yönetim-sistemi">Türkçe</a> • <a href="#-bus-management-system">English</a>
</div>

---

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
    ```bash
    pip install -r requirements.txt
    ```

4.  **Uygulamayı Çalıştırın**
    ```bash
    python main.py
    ```

## 📂 Proje Yapısı

```
OtobusKontrolSistemi/
├── .venv/
├── app/
│   ├── assets/
│   │   └── bus.png
│   ├── __init__.py
│   ├── classes.py
│   ├── main.py
│   └── utils.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🤝 Katkıda Bulunma

Katkılarınız projeyi daha iyi hale getirecektir! Lütfen bir "pull request" açmaktan veya "issue" oluşturmaktan çekinmeyin.

1.  Projeyi **Fork** edin.
2.  Yeni bir **Branch** oluşturun (`git checkout -b ozellik/YeniOzellik`).
3.  Değişikliklerinizi **Commit** edin (`git commit -m 'Yeni bir özellik eklendi'`).
4.  Oluşturduğunuz **Branch**'i **Push** edin (`git push origin ozellik/YeniOzellik`).
5.  Bir **Pull Request** açın.

## 📝 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

---
---

<div align="center">
  <a href="#-otobüs-yönetim-sistemi">Türkçe</a> • <a href="#-bus-management-system">English</a>
</div>

# 🚌 Bus Management System

This project is a comprehensive desktop management application for bus companies, developed using Python and the PyQt5 library. The application allows for easy tracking of critical operations such as company, bus, route, passenger, and ticket management.

## ✨ Key Features

-   **Multi-Company Support**: Different companies can be selected or new ones can be created at the start of the application.
-   **Company Dashboard**: Company information (address, tax ID, etc.) can be updated. Statistics like the total number of buses, routes, and passengers can be tracked in real-time.
-   **Bus Fleet Management**:
    -   Add, update, and delete bus information (brand, model, capacity).
    -   Manage the status of buses (In Garage, On Route, In Maintenance, etc.).
-   **Route and Schedule Planning**:
    -   Create new routes with detailed information (departure-arrival points, time, itinerary).
    -   Assign available buses to routes.
-   **Passenger Management**:
    -   Save, update, and delete passenger information (ID Number, contact info).
-   **Ticket Sales and Management**:
    -   Issue tickets to passengers for existing routes.
    -   Manage ticket details (seat no, fare, PNR code, payment status).
-   **Modern and User-Friendly Interface**:
    -   Easy navigation between modules with a tabbed structure.
    -   Stylish dark theme support with the `qdarktheme` library.

## 🛠️ Technologies Used

-   **Python 3**: The main programming language.
-   **PyQt5**: The library used for the desktop application interface.
-   **qdarktheme**: The library used to provide a modern dark theme.

## 🚀 Setup and Execution

Follow the steps below to run the project on your local machine.

### Prerequisites

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### Step-by-Step Installation

1.  **Clone the Project**
    ```bash
    git clone [https://github.com/emrecor/OtobusKontrolSistemi.git](https://github.com/emrecor/OtobusKontrolSistemi.git)
    cd OtobusKontrolSistemi
    ```

2.  **Create and Activate a Virtual Environment** (Recommended)
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Required Libraries**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    python main.py
    ```

## 📂 Project Structure

```
OtobusKontrolSistemi/
├── .venv/                  # Virtual environment folder
├── app/
│   ├── assets/             # Visual assets, icons etc.
│   │   └── bus.png
│   ├── __init__.py
│   ├── classes.py          # Main classes (Company, Bus, Route, etc.)
│   ├── main.py             # UI and control flow
│   └── utils.py            # Helper functions
├── .gitignore              # Ignored by Git
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

## 🤝 Contributing

Contributions will make the project better! Please feel free to open a "pull request" or create an "issue".

1.  **Fork** the project.
2.  Create a new **Branch** (`git checkout -b feature/NewFeature`).
3.  **Commit** your changes (`git commit -m 'Add a new feature'`).
4.  **Push** your branch (`git push origin feature/NewFeature`).
5.  Open a **Pull Request**.

## 📝 License

This project is licensed under the MIT License.
