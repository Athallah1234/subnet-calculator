<div align="center">

# 🌐 Simple Subnet Calculator

**IPv4 / IPv6 / CIDR Network Calculator**

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.5%2B-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-pytest-red?style=for-the-badge&logo=pytest&logoColor=white)](#-menjalankan-tests)
[![Offline](https://img.shields.io/badge/Offline-100%25-success?style=for-the-badge)](#-100-offline)

*Aplikasi desktop modern, bersih, dan ringan untuk perhitungan jaringan IPv4, IPv6, dan CIDR.*
*Dirancang untuk **Network Engineer**, **System Administrator**, **Programmer**, **Mahasiswa IT**, dan siapa pun yang ingin memahami jaringan komputer.*

</div>

---

## 📋 Daftar Isi

- [✨ Tentang Aplikasi](#-tentang-aplikasi)
- [🚀 Fitur Unggulan](#-fitur-unggulan)
- [📁 Struktur Proyek](#-struktur-proyek)
- [🧩 Arsitektur & Desain](#-arsitektur--desain)
- [⚙️ Requirements](#️-requirements)
- [📦 Instalasi](#-instalasi)
- [▶️ Menjalankan Aplikasi](#️-menjalankan-aplikasi)
- [🧪 Menjalankan Tests](#-menjalankan-tests)
- [📦 Build Executable](#-build-executable)
- [🔑 Keyboard Shortcuts](#-keyboard-shortcuts)
- [📖 Panduan Penggunaan](#-panduan-penggunaan)
- [🔢 Contoh Perhitungan](#-contoh-perhitungan)
- [🧠 Detail Teknis Kalkulator](#-detail-teknis-kalkulator)
- [🎨 Sistem UI & Tema](#-sistem-ui--tema)
- [💾 Penyimpanan Data Lokal](#-penyimpanan-data-lokal)
- [📚 Referensi CIDR IPv4](#-referensi-cidr-ipv4)
- [❓ FAQ](#-faq-frequently-asked-questions)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Kontribusi](#-kontribusi)
- [📄 Lisensi](#-lisensi)

---

## ✨ Tentang Aplikasi

**Simple Subnet Calculator** adalah aplikasi desktop berbasis **Python + PySide6** yang membantu Anda melakukan perhitungan jaringan komputer dengan cepat, akurat, dan mudah — sepenuhnya **offline tanpa internet**.

Aplikasi ini menggabungkan lima alat jaringan dalam satu antarmuka yang bersih:

| Alat | Keterangan |
|---|---|
| **IPv4 Calculator** | Hitung semua detail jaringan IPv4 dari prefix `/0` hingga `/32` |
| **IPv6 Calculator** | Hitung detail jaringan IPv6 hingga prefix `/128` |
| **CIDR Calculator** | Antarmuka terpadu yang mendukung notasi IPv4 maupun IPv6 |
| **IPv4 Subnetting** | Pecah jaringan IPv4 menjadi subnet-subnet kecil secara dinamis |
| **Prefix Reference** | Tabel referensi lengkap semua 33 prefix CIDR IPv4 |

---

## 🚀 Fitur Unggulan

### 🔵 IPv4 Subnet Calculator
- ✅ Menghitung **Network Address**, **Broadcast Address**, **Subnet Mask**, **Wildcard Mask**
- ✅ Menampilkan **First Usable Host** dan **Last Usable Host**
- ✅ Menghitung **Total Addresses** dan **Usable Hosts** (format ribuan)
- ✅ Dukungan penuh prefix `/0` hingga `/32`
- ✅ Penanganan khusus `/31` (RFC 3021 — 2 host tanpa broadcast) dan `/32` (host route)
- ✅ **Representasi Binary** lengkap: IP binary, serta pemisah `Network Bits | Host Bits`
- ✅ **Klasifikasi jaringan** otomatis: Private/Public, Loopback, Link-Local, Multicast, Reserved, Unspecified, Global, Documentation

### 🟣 IPv6 Subnet Calculator
- ✅ Menampilkan alamat **Compressed** (format pendek) dan **Expanded/Exploded** (format 128-bit penuh)
- ✅ Menghitung **Network Address**, **First Address**, **Last Address**
- ✅ Menghitung **Total Addresses** untuk semua prefix `/0` hingga `/128`
- ✅ Menampilkan info **Prefix Length**, **Network Bits**, dan **Interface Bits**
- ✅ Klasifikasi otomatis: Global Unicast, Unique Local (ULA), Link-Local, Loopback, Multicast, Unspecified, Documentation (`2001:db8::/32`)

### 🟡 CIDR Calculator
- ✅ Antarmuka tunggal yang **mendeteksi otomatis** versi IP (IPv4 atau IPv6)
- ✅ Mendukung format input `192.168.1.0/24` maupun `2001:db8::1/64`
- ✅ Menampilkan semua detail jaringan dengan output yang sesuai versi IP

### 🔀 IPv4 Subnetting
- ✅ Memecah jaringan IPv4 mana pun menjadi subnet-subnet yang lebih kecil
- ✅ Pilih **New Prefix** secara interaktif via dropdown (dari prefix base hingga `/32`)
- ✅ Tabel subnet dinamis dengan kolom: Subnet #, Network Range, First Host, Last Host, Broadcast
- ✅ **Perlindungan UI**: konfirmasi otomatis jika jumlah subnet > **1.024** (mencegah freeze)
- ✅ Penanganan edge case `/31` dan `/32` dalam subnetting

### 🎯 Device Count → Auto Prefix
- ✅ Input **jumlah perangkat** → aplikasi otomatis menghitung dan memilih prefix terkecil yang cukup
- ✅ Formula IPv4: `prefix = 32 - ceil(log2(n + 2))`
- ✅ Formula IPv6: `prefix = 128 - ceil(log2(n))`
- ✅ Memudahkan perencanaan jaringan tanpa menghitung manual

### 📊 Prefix Reference Table
- ✅ Tabel referensi CIDR lengkap `/0` hingga `/32` (33 baris)
- ✅ Kolom: **Prefix**, **Subnet Mask**, **Wildcard Mask**, **Total Addresses**, **Usable Hosts**
- ✅ Semua nilai dengan format ribuan yang mudah dibaca

### 🌗 Dark / Light Mode
- ✅ Toggle **Dark Mode ↔ Light Mode** instan tanpa restart
- ✅ Preferensi tema tersimpan otomatis ke disk dan diingat saat restart
- ✅ Desain modern dengan palet warna yang cermat dan tipografi bersih (Segoe UI)

### 📋 Export & Copy Results
- ✅ **Copy to Clipboard** — Salin hasil ke clipboard sebagai TXT terstruktur
- ✅ **Save as TXT** — Simpan hasil sebagai file `.txt` yang terbaca manusia
- ✅ **Export as JSON** — Export data ke format `.json` (cocok untuk integrasi/scripting)

### 🕰️ History Panel
- ✅ Panel riwayat di sisi kanan (bisa di-resize via splitter)
- ✅ Menyimpan hingga **20 riwayat** perhitungan terakhir secara persisten
- ✅ **Double-click** untuk memuat ulang perhitungan dari riwayat
- ✅ Hapus item individual atau **Clear All** sekaligus

### ⌨️ Keyboard Shortcuts
- ✅ Shortcut native untuk semua operasi utama

### 🌐 100% Offline
- ✅ Tidak memerlukan koneksi internet
- ✅ Tidak mengirim data ke mana pun
- ✅ Semua perhitungan dilakukan lokal via Python Standard Library `ipaddress`

---

## 📁 Struktur Proyek

```text
network-tools/                        ← Root proyek
├── main.py                           ← Entry point aplikasi
├── requirements.txt                  ← Daftar dependensi Python
├── README.md                         ← Dokumentasi proyek (file ini)
├── LICENSE                           ← Lisensi MIT
│
├── src/                              ← Source code utama
│   ├── __init__.py
│   ├── app.py                        ← Bootstrap QApplication + MainWindow
│   │
│   ├── calculator/                   ← Engine perhitungan (pure Python, tanpa UI)
│   │   ├── __init__.py
│   │   ├── ipv4.py                   ← Kalkulator IPv4 + subnetting
│   │   ├── ipv6.py                   ← Kalkulator IPv6
│   │   └── cidr.py                   ← CIDR wrapper (auto-detect IPv4/IPv6)
│   │
│   ├── ui/                           ← Komponen antarmuka (PySide6)
│   │   ├── __init__.py
│   │   ├── main_window.py            ← MainWindow utama (~780 baris)
│   │   ├── widgets.py                ← Custom widgets: InfoCard, SubnetTable
│   │   └── styles.py                 ← QSS stylesheet (Dark + Light theme)
│   │
│   └── utils/                        ← Utilitas pendukung
│       ├── __init__.py
│       ├── validators.py             ← Validasi input IP/CIDR
│       └── formatters.py             ← Format output (TXT, JSON, angka)
│
└── tests/                            ← Unit test otomatis (pytest)
    ├── test_ipv4.py                  ← Test kalkulator IPv4 (4 test cases)
    ├── test_ipv6.py                  ← Test kalkulator IPv6
    └── test_cidr.py                  ← Test kalkulator CIDR
```

---

## 🧩 Arsitektur & Desain

Proyek mengikuti arsitektur **layered / separation of concerns**:

```
┌─────────────────────────────────────────────┐
│           main.py  (Entry Point)             │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         src/app.py  (App Bootstrap)          │
│       QApplication + MainWindow setup        │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│         src/ui/  (Presentation Layer)        │
│  main_window.py ← widgets.py ← styles.py    │
└──────────────────┬──────────────────────────┘
                   │ calls
┌──────────────────▼──────────────────────────┐
│     src/calculator/  (Business Logic)        │
│       ipv4.py    ipv6.py    cidr.py          │
└──────────────────┬──────────────────────────┘
                   │ validated by
┌──────────────────▼──────────────────────────┐
│        src/utils/  (Support Layer)           │
│        validators.py    formatters.py        │
└─────────────────────────────────────────────┘
```

**Prinsip desain utama:**
- 🔒 **Calculator layer** = **pure functions** — bebas dependensi UI, mudah di-test dan di-reuse
- 🎨 **UI layer** hanya menampilkan data dan merespons event user
- ✅ **Validators** membersihkan & memvalidasi input sebelum masuk kalkulasi
- 📄 **Formatters** memisahkan logika presentasi output dari logika bisnis

---

## ⚙️ Requirements

| Komponen | Versi Minimum | Keterangan |
|---|---|---|
| **Python** | `3.12+` | Diperlukan untuk `ipaddress` yang stabil |
| **PySide6** | `>= 6.5.0` | Framework GUI Qt6 untuk Python |
| **pytest** | `>= 8.0.0` | Framework unit testing (opsional, untuk dev) |
| **PyInstaller** | `latest` | Opsional, untuk build standalone `.exe` |

> **Catatan:** Aplikasi menggunakan modul `ipaddress` dari **Python Standard Library** — tidak perlu library jaringan eksternal apa pun.

---

## 📦 Instalasi

### 1. Clone Repositori

```bash
git clone https://github.com/Athallah1234/subnet-calculator.git
cd subnet-calculator
```

Atau unduh ZIP dari GitHub dan ekstrak ke folder pilihan Anda.

### 2. Buat Virtual Environment

```bash
python -m venv .venv
```

### 3. Aktifkan Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

Setelah aktif, prompt terminal akan menampilkan `(.venv)` di depannya.

### 4. Install Dependensi

```bash
pip install -r requirements.txt
```

Output yang diharapkan:
```
Successfully installed PySide6-6.x.x PySide6-Addons-6.x.x shiboken6-6.x.x pytest-8.x.x
```

---

## ▶️ Menjalankan Aplikasi

Pastikan virtual environment sudah aktif, lalu:

```bash
python main.py
```

Aplikasi terbuka sebagai jendela desktop dengan ukuran minimum **950 × 700 px**. Tema default adalah **Dark Mode**.

---

## 🧪 Menjalankan Tests

Proyek dilengkapi unit test otomatis menggunakan **pytest**:

```bash
# Jalankan semua test
pytest

# Verbose output
pytest -v

# Test spesifik per file
pytest tests/test_ipv4.py -v
pytest tests/test_ipv6.py -v
pytest tests/test_cidr.py -v
```

**Contoh output sukses:**
```
=============================== test session starts ================================
platform win32 -- Python 3.12.x, pytest-8.x.x
collected 7 items

tests/test_cidr.py .                                                         [ 14%]
tests/test_ipv4.py ....                                                      [ 71%]
tests/test_ipv6.py ..                                                        [100%]

================================ 7 passed in 0.15s =================================
```

### Test Cases yang Dicakup

| File | Test Case | Keterangan |
|---|---|---|
| `test_ipv4.py` | `test_calculate_ipv4_24` | Perhitungan standar `/24` |
| `test_ipv4.py` | `test_calculate_ipv4_31` | Edge case `/31` (RFC 3021) |
| `test_ipv4.py` | `test_calculate_ipv4_32` | Edge case `/32` (host route) |
| `test_ipv4.py` | `test_subnet_ipv4` | Subnetting `/24` → `/26` (4 subnet) |
| `test_ipv6.py` | IPv6 basic | Kalkulasi IPv6 dasar |
| `test_cidr.py` | CIDR auto-detect | Auto-detect IPv4 vs IPv6 |

---

## 📦 Build Executable

Kemas menjadi file **`.exe` standalone** tanpa perlu Python di komputer tujuan:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Build

```bash
pyinstaller --onefile --windowed --name=SimpleSubnetCalculator main.py
```

| Flag | Keterangan |
|---|---|
| `--onefile` | Kemas semua ke dalam satu file `.exe` |
| `--windowed` | Jalankan tanpa jendela konsol (GUI only) |
| `--name=...` | Nama file output |

### 3. Lokasi Output

```
dist/
└── SimpleSubnetCalculator.exe    ← Siap distribusi (Windows)
```

> **Catatan:** Ukuran `.exe` biasanya **60–100 MB** karena menyertakan runtime PySide6. Dapat dijalankan di komputer lain tanpa instalasi Python.

**Build untuk platform lain:**
```bash
# macOS / Linux
pyinstaller --onefile --windowed --name=SimpleSubnetCalculator main.py
```

---

## 🔑 Keyboard Shortcuts

| Shortcut | Aksi |
|---|---|
| `Ctrl + Enter` | ▶ Hitung / Calculate |
| `Ctrl + L` | 🗑️ Bersihkan Input Fields |
| `Ctrl + C` | 📋 Copy Hasil ke Clipboard |
| `Ctrl + S` | 💾 Simpan Hasil sebagai TXT |
| `Ctrl + H` | 👁️ Tampilkan/Sembunyikan History Panel |
| `Ctrl + Q` | ❌ Keluar dari Aplikasi |

---

## 📖 Panduan Penggunaan

### IPv4 Calculator

1. Pastikan **Calculator Type** dropdown diatur ke `IPv4`
2. Masukkan alamat IP di field **"IP Address / CIDR"**, contoh:
   - `192.168.1.10` (tanpa prefix → gunakan dropdown Default Prefix)
   - `192.168.1.10/24` (dengan prefix langsung di input)
   - `10.0.0.1/8` atau `172.16.5.100/16`
3. Opsional: isi **"Jumlah Perangkat"** → prefix otomatis disesuaikan
4. Klik **"Calculate"** atau tekan `Ctrl + Enter`
5. Hasil ditampilkan di kartu: **Basic Information**, **Classification**, **Binary Representation**

### IPv6 Calculator

1. Ubah **Calculator Type** ke `IPv6`
2. Masukkan alamat IPv6, contoh:
   - `2001:db8::1/64` | `fe80::1/10` | `fc00::1/7` | `::1/128`
3. Pilih prefix dari dropdown (range `/0`–`/128`, default `/64`)
4. Klik **"Calculate"**
5. Hasil menampilkan alamat Compressed & Expanded, range, dan klasifikasi

> Tab **IPv4 Subnetting** otomatis disembunyikan saat mode IPv6 aktif.

### CIDR Calculator

1. Ubah **Calculator Type** ke `CIDR`
2. Masukkan dalam notasi CIDR — IPv4 atau IPv6:
   - `192.168.100.0/22` | `2001:db8::/32`
3. Klik **"Calculate"** — versi IP terdeteksi otomatis

### IPv4 Subnetting

1. Lakukan kalkulasi IPv4 terlebih dahulu
2. Scroll ke kartu **"IPv4 Subnetting"**
3. Pilih **New Prefix** dari dropdown
4. Klik **"Calculate Subnets"**
5. Tabel menampilkan: Subnet #, Network Range, First Host, Last Host, Broadcast

> ⚠️ Jika jumlah subnet > **1.024**, muncul dialog konfirmasi untuk mencegah UI freeze.

### Prefix Reference Table

Klik tab **"Prefix Reference Table"** — tabel 33 baris prefix IPv4 (`/0`–`/32`) dengan Subnet Mask, Wildcard, Total Addresses, dan Usable Hosts.

### History Panel

- Toggle dengan `Ctrl + H` atau **View → Toggle History Panel**
- **Double-click** item → muat ulang perhitungan otomatis
- **Delete** → hapus item terpilih | **Clear All** → hapus semua
- Maks **20 entri** terbaru, tersimpan persisten ke disk

### Export & Copy Results

| Tombol | Fungsi |
|---|---|
| **Copy Result** | Salin ke clipboard (format TXT terstruktur) |
| **Save TXT** | Dialog simpan → file `.txt` |
| **Export JSON** | Dialog simpan → file `.json` |

---

## 🔢 Contoh Perhitungan

### Contoh IPv4 — `192.168.1.10/24`

| Field | Hasil |
|---|---|
| IP Address | `192.168.1.10` |
| CIDR Prefix | `/24` |
| Subnet Mask | `255.255.255.0` |
| Wildcard Mask | `0.0.0.255` |
| Network Address | `192.168.1.0` |
| Broadcast Address | `192.168.1.255` |
| First Usable Host | `192.168.1.1` |
| Last Usable Host | `192.168.1.254` |
| Total Addresses | `256` |
| Usable Hosts | `254` |
| Address Type | `Private IPv4` |
| Scope | `Private Network` |

**Binary:**
```
IP Binary   : 11000000.10101000.00000001.00001010
Network|Host: 11000000.10101000.00000001 | 00001010
```

### Contoh IPv6 — `2001:db8::1/64`

| Field | Hasil |
|---|---|
| Compressed | `2001:db8::1` |
| Expanded | `2001:0db8:0000:0000:0000:0000:0000:0001` |
| Network Address | `2001:db8::` |
| First Address | `2001:db8::` |
| Last Address | `2001:db8::ffff:ffff:ffff:ffff` |
| Total Addresses | `18,446,744,073,709,551,616` |
| Address Type | `Documentation` |

### Contoh Subnetting — `192.168.1.0/24` → `/26`

| Info | Nilai |
|---|---|
| Jumlah Subnet | `4` |
| Addresses/Subnet | `64` |
| Usable Hosts/Subnet | `62` |

| # | Network | First Host | Last Host | Broadcast |
|---|---|---|---|---|
| 1 | `192.168.1.0/26` | `192.168.1.1` | `192.168.1.62` | `192.168.1.63` |
| 2 | `192.168.1.64/26` | `192.168.1.65` | `192.168.1.126` | `192.168.1.127` |
| 3 | `192.168.1.128/26` | `192.168.1.129` | `192.168.1.190` | `192.168.1.191` |
| 4 | `192.168.1.192/26` | `192.168.1.193` | `192.168.1.254` | `192.168.1.255` |

---

## 🧠 Detail Teknis Kalkulator

### IPv4 Engine — `src/calculator/ipv4.py`

#### `calculate_ipv4(ip_str, prefix) → Dict`

```python
from src.calculator.ipv4 import calculate_ipv4

result = calculate_ipv4("192.168.1.10", 24)
# result["network_address"]        → "192.168.1.0"
# result["broadcast_address"]      → "192.168.1.255"
# result["subnet_mask"]            → "255.255.255.0"
# result["wildcard_mask"]          → "0.0.0.255"
# result["number_of_usable_hosts"] → 254
# result["classification"]["address_type"] → "Private IPv4"
# result["binary"]["network_host"] → "11000000.10101000.00000001 | 00001010"
```

**Penanganan Edge Cases:**

| Prefix | Total | Usable | Broadcast |
|---|---|---|---|
| `/32` | 1 | 1 | N/A (host route) |
| `/31` | 2 | 2 | N/A (RFC 3021, P2P) |
| `/30` | 4 | 2 | Normal |
| `/0` | 4,294,967,296 | 4,294,967,294 | Normal |

#### `subnet_ipv4(network_str, new_prefix) → Dict`

```python
from src.calculator.ipv4 import subnet_ipv4

result = subnet_ipv4("192.168.1.0/24", 26)
# result["number_of_subnets"]    → 4
# result["addresses_per_subnet"] → 64
# result["usable_hosts"]         → 62
# result["subnets"][0]["network"] → "192.168.1.0/26"
```

### IPv6 Engine — `src/calculator/ipv6.py`

#### `calculate_ipv6(ip_str, prefix) → Dict`

```python
from src.calculator.ipv6 import calculate_ipv6

result = calculate_ipv6("2001:db8::1", 64)
# result["compressed_address"]  → "2001:db8::1"
# result["expanded_address"]    → "2001:0db8:0000:..."
# result["number_of_addresses"] → 18446744073709551616
```

**Klasifikasi IPv6:**

| Range | Tipe |
|---|---|
| `::1/128` | Loopback |
| `fe80::/10` | Link-Local Unicast |
| `fc00::/7` / `fd00::/8` | Unique Local Address (ULA) |
| `ff00::/8` | Multicast |
| `2001:db8::/32` | Documentation |
| `2000::/3` | Global Unicast |

### CIDR Engine — `src/calculator/cidr.py`

#### `calculate_cidr(ip_or_network, prefix) → Dict`

Auto-detect versi IP dan delegasi ke engine yang sesuai:

```python
from src.calculator.cidr import calculate_cidr

r4 = calculate_cidr("10.0.0.1", 8)
# r4["version"] → 4

r6 = calculate_cidr("2001:db8::1", 64)
# r6["version"] → 6
```

### Validators — `src/utils/validators.py`

#### `validate_cidr_input(ip_str) → Tuple[bool, str, Optional[int]]`

```python
from src.utils.validators import validate_cidr_input

# Valid dengan prefix
validate_cidr_input("192.168.1.10/24") → (True, "192.168.1.10/24", 24)

# Valid tanpa prefix
validate_cidr_input("192.168.1.10")    → (True, "192.168.1.10", None)

# Invalid
validate_cidr_input("256.0.0.1/24")   → (False, "Invalid IP address format: 256.0.0.1", None)
```

**Validasi yang dilakukan:**
- Input tidak boleh kosong
- Tidak boleh ada lebih dari satu `/`
- Format IP harus valid (dicoba IPv4 dahulu, lalu IPv6)
- Prefix IPv4: `0`–`32` | Prefix IPv6: `0`–`128`
- Prefix harus bilangan bulat

### Formatters — `src/utils/formatters.py`

| Fungsi | Keterangan |
|---|---|
| `format_number(val)` | Format integer dengan pemisah ribuan: `4294967296` → `"4,294,967,296"` |
| `format_to_txt(data)` | Hasilkan representasi TXT terstruktur dari dict kalkulasi |
| `format_to_json(data)` | Serialize dict ke JSON string dengan indentasi 2 spasi |

---

## 🎨 Sistem UI & Tema

**File:** `src/ui/styles.py` — menggunakan **Qt Stylesheet (QSS)**

### Dark Theme (Default)

| Element | Warna |
|---|---|
| Background utama | `#121214` |
| Card / GroupBox | `#1e1e24` |
| Input / Button | `#27272a` |
| Border | `#2d2d34` |
| Teks utama | `#e4e4e7` |
| Teks muted | `#a1a1aa` |
| Tombol Calculate | `#097969` (hijau gelap) |
| Tombol Clear | `#7f1d1d` (merah gelap) |

### Light Theme

| Element | Warna |
|---|---|
| Background utama | `#f4f4f5` |
| Card / GroupBox | `#ffffff` |
| Input / Button | `#ffffff` |
| Border | `#d4d4d8` |
| Teks utama | `#18181b` |
| Teks muted | `#71717a` |
| Tombol Calculate | `#10b981` (hijau cerah) |
| Tombol Clear | `#ef4444` (merah cerah) |

**Font stack:** `Segoe UI` → `-apple-system` → `BlinkMacSystemFont` → `Roboto` → `Helvetica` → `Arial`

### Custom Widgets (`src/ui/widgets.py`)

**`InfoCard(QGroupBox)`** — Card key-value yang bersih:
- `add_row(key, label)` — tambah baris label:nilai
- `update_val(key, val)` — update nilai secara dinamis
- `clear_vals()` — reset semua nilai ke `"-"`

**`SubnetTable(QTableWidget)`** — Tabel subnet dinamis:
- `populate(subnet_list)` — isi tabel dengan data subnet
- `clear_table()` — kosongkan tabel

---

## 💾 Penyimpanan Data Lokal

Aplikasi menyimpan data pengguna di:

```
Windows: C:\Users\<Username>\.gemini\antigravity\simple-subnet-calculator\
├── config.json      ← Preferensi tema
└── history.json     ← Riwayat perhitungan (maks 20 entri)
```

**`config.json`:**
```json
{ "dark_mode": true }
```

**`history.json`:**
```json
[
  { "input": "192.168.1.10/24", "type": "IPv4" },
  { "input": "2001:db8::1/64",  "type": "IPv6" },
  { "input": "10.0.0.0/8",      "type": "CIDR" }
]
```

> **Privasi:** Tidak ada data yang dikirim ke server eksternal. Semua data 100% lokal.

---

## 📚 Referensi CIDR IPv4

### Prefix Umum

| Prefix | Subnet Mask | Wildcard | Total Addresses | Usable Hosts |
|---|---|---|---|---|
| `/8` | `255.0.0.0` | `0.255.255.255` | 16,777,216 | 16,777,214 |
| `/16` | `255.255.0.0` | `0.0.255.255` | 65,536 | 65,534 |
| `/24` | `255.255.255.0` | `0.0.0.255` | 256 | 254 |
| `/25` | `255.255.255.128` | `0.0.0.127` | 128 | 126 |
| `/26` | `255.255.255.192` | `0.0.0.63` | 64 | 62 |
| `/27` | `255.255.255.224` | `0.0.0.31` | 32 | 30 |
| `/28` | `255.255.255.240` | `0.0.0.15` | 16 | 14 |
| `/29` | `255.255.255.248` | `0.0.0.7` | 8 | 6 |
| `/30` | `255.255.255.252` | `0.0.0.3` | 4 | 2 |
| `/31` | `255.255.255.254` | `0.0.0.1` | 2 | 2 (RFC 3021) |
| `/32` | `255.255.255.255` | `0.0.0.0` | 1 | 1 (host route) |

### Private IP Ranges (RFC 1918)

| Range | CIDR |
|---|---|
| `10.0.0.0` – `10.255.255.255` | `10.0.0.0/8` |
| `172.16.0.0` – `172.31.255.255` | `172.16.0.0/12` |
| `192.168.0.0` – `192.168.255.255` | `192.168.0.0/16` |

---

## ❓ FAQ (Frequently Asked Questions)

**Q: Apakah aplikasi ini membutuhkan koneksi internet?**
> Tidak sama sekali. Semua perhitungan dilakukan lokal via Python Standard Library `ipaddress`. Aplikasi 100% offline.

**Q: Bisakah saya menggunakan modul calculator tanpa UI?**
> Ya! Fungsi di `src/calculator/` adalah pure functions bebas PySide6:
> ```python
> from src.calculator.ipv4 import calculate_ipv4
> result = calculate_ipv4("192.168.1.1", 24)
> ```

**Q: Kenapa `/31` berbeda dari `/30`?**
> `/31` mengikuti **RFC 3021** — hanya ada 2 alamat, tidak ada network/broadcast. Ideal untuk link point-to-point yang lebih hemat IP dibanding `/30`.

**Q: Kenapa saat subnet banyak ada konfirmasi dulu?**
> Untuk mencegah UI freeze. Contoh: `/16` → `/32` menghasilkan 65.536 baris tabel. Batas konfirmasi adalah **1.024 subnet**.

**Q: Di mana file config dan history disimpan?**
> `C:\Users\<Username>\.gemini\antigravity\simple-subnet-calculator\`. Lihat [Penyimpanan Data Lokal](#-penyimpanan-data-lokal).

**Q: Apakah ada dukungan IPv6 Subnetting?**
> Belum. Tab Subnetting hanya aktif untuk IPv4. IPv6 subnetting menjadi kandidat fitur versi berikutnya.

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'PySide6'`
```bash
# Aktifkan virtual environment terlebih dahulu
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

pip install -r requirements.txt
```

### `ModuleNotFoundError: No module named 'src'`
Selalu jalankan dari **root direktori proyek**:
```bash
# ✅ Benar
cd simple-subnet-calculator
python main.py

# ❌ Salah
cd src && python app.py
```

### Error Parsing Input
Gunakan format yang benar:
- IPv4: `192.168.1.10` atau `192.168.1.10/24`
- IPv6: `2001:db8::1` atau `2001:db8::1/64`
- CIDR: `10.0.0.0/8` atau `2001:db8::/32`

### Aplikasi Crash / Tidak Terbuka
```bash
python --version  # Harus >= 3.12
pip show PySide6  # Cek versi PySide6 >= 6.5.0
```

### History / Tema Tidak Tersimpan
Pastikan Anda memiliki akses **tulis** ke folder:
`C:\Users\<Username>\.gemini\antigravity\simple-subnet-calculator\`

---

## 🤝 Kontribusi

Kontribusi sangat disambut! Berikut panduan singkatnya:

### Alur Kontribusi

```bash
# 1. Fork repositori, lalu clone
git clone https://github.com/Athallah1234/subnet-calculator.git

# 2. Buat branch baru
git checkout -b feature/nama-fitur

# 3. Buat perubahan, tambahkan test
pytest -v  # Pastikan semua test lulus

# 4. Commit & push
git commit -m "feat: deskripsi fitur baru"
git push origin feature/nama-fitur

# 5. Buat Pull Request ke branch main
```

### Konvensi Kode
- Gunakan **type hints** untuk semua fungsi
- Tambahkan **docstring** untuk fungsi baru
- Ikuti **PEP 8**
- Jangan campur logika UI ke modul `calculator/`
- Tambahkan **unit test** untuk setiap fungsi kalkulator baru

### Ide Fitur untuk Dikontribusikan

- [ ] IPv6 Subnetting
- [ ] CIDR Aggregation / Supernetting
- [ ] Export ke format CSV
- [ ] "Which subnet am I in?" — cari subnet yang memuat sebuah IP
- [ ] Dark/Light mode auto-detect dari OS
- [ ] Internasionalisasi (i18n) — multi-bahasa

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **MIT License** — bebas digunakan, dimodifikasi, dan didistribusikan.

```
MIT License

Copyright (c) 2026 Simple Subnet Calculator Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Lihat file [LICENSE](LICENSE) untuk teks lengkap.

---

<div align="center">

**Dibuat dengan ❤️ menggunakan Python + PySide6**

*Jika proyek ini bermanfaat, berikan ⭐ di GitHub!*

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat-square&logo=python)](https://python.org)
[![PySide6](https://img.shields.io/badge/PySide6-Qt6-41CD52?style=flat-square&logo=qt)](https://doc.qt.io/qtforpython/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

