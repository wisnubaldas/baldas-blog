# Blog & Portofolio Pribadi — Wisnu Hidayat

Situs web personal resmi **Wisnu Hidayat** (`wisnubaldas.net`) yang menggabungkan halaman **Company Profile / Portofolio One-Page Parallax** dan **Blog Publik**.

Dikembangkan menggunakan **Django 6.0.7**, **HTMX**, dan **SQLite (Dev) / Supabase PostgreSQL (Prod)** dengan pendekatan **MVT Murni** (Model-View-Template).

---

## 🚀 Fitur Utama

### 🏢 1. Company Profile / Portofolio (`/`)
- **One-Page Parallax UI**: Efek scroll-spy, parallax background, dan animasi responsif berbasis `one-page-parallax` theme.
- **Section Profil**: Hero Banner, Tentang Saya, Ringkasan Keahlian (Progress Bar), Pengalaman Kerja & Pendidikan, Layanan, Portofolio Proyek, dan Form Kontak.
- **Form Kontak Dynamic (HTMX)**: Pengiriman pesan instan tanpa reload halaman, dilengkapi validasi server-side dan otomatis tersimpan di database (`ContactMessage`).
- **CMS Admin**: Pengelolaan data profil, skill, timeline pengalaman, proyek portofolio, dan pesan masuk.

### 📝 2. Blog Teknis & Catatan (`/blog/`)
- **Indeks & Grid View**: Tampilan artikel publik dengan waktu baca, tanggal rilis, gambar sampul, dan pagination.
- **Live Search HTMX**: Pencarian artikel secara *real-time* berbasis keyword tanpa reload halaman.
- **Kategori & Tagging**: Filter artikel berdasarkan kategori dan tag teknis.
- **Detail Artikel Kaya Format**: Editor `django-ckeditor-5`, breadcrumb, tombol share media sosial, dan rekomendasi artikel terkait.
- **Halaman Statis**: Halaman About Me & Kontak khusus konteks blog.

---

## 🛠️ Stack Teknologi

- **Backend**: Python 3.12, Django 6.0.7
- **Frontend Interaktivitas**: HTMX 1.9.12 (Server-Driven UI)
- **Styling & Theme**: Vanilla CSS, Bootstrap, Color Admin Parallax & Blog Themes
- **Rich Text Editor**: `django-ckeditor-5`
- **Database**:
  - Development Lokal: SQLite (`db.sqlite3`)
  - Production Server: Supabase PostgreSQL 17.6 (Connection Pooler Port 6543)
- **Static Files Storage**: WhiteNoise (`CompressedManifestStaticFilesStorage`)
- **Deployment Platform**: Vercel (Serverless WSGI via `api/index.py`)

---

## 📂 Struktur Proyek

Proyek Django terletak di dalam direktori `django/` dengan struktur modular:

```text
blog-baldas/
├── AGENTS.md                         # Instruksi & kontrak kerja agent
├── README.md                         # Dokumentasi utama repository
└── django/                           # Root aplikasi Django
    ├── manage.py
    ├── config/                       # Settings, root URLs, ASGI/WSGI
    │   ├── settings.py               # Flexible config (SQLite/PostgreSQL)
    │   └── urls.py
    ├── apps/
    │   ├── company_profile/          # App Portofolio Parallax
    │   │   ├── controllers/          # Home, Profile, Portfolio, Contact
    │   │   ├── models/               # Profile, Skill, Experience, Project, ContactMessage
    │   │   ├── urls/                 # Home, Portfolio, Contact URLs
    │   │   ├── templates/company_profile/
    │   │   └── static/company_profile/
    │   └── blog/                     # App Blog Mandiri
    │       ├── controllers/          # Post, Category, Search, Page
    │       ├── models/               # Post, Category, Tag
    │       ├── urls/                 # Post, Category, Search, Page URLs
    │       ├── templates/blog/
    │       └── static/blog/
    ├── templates/                    # Base templates
    ├── static/                       # Global static assets
    ├── media/                        # User uploads (media)
    ├── api/
    │   └── index.py                  # Entry point WSGI Vercel
    ├── vercel.json                   # Konfigurasi deployment Vercel
    ├── .env.example                  # Template variabel lingkungan
    ├── requirements.txt
    └── db.sqlite3                    # Database lokal (gitignored)
```

---

## 💻 Panduan Jalankan di Lokal (Development)

### 1. Clone & Setup Virtual Environment
```bash
git clone https://github.com/wisnubaldas/blog-baldas.git
cd blog-baldas/django

# Buat & aktifkan virtualenv
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Salin `.env.example` menjadi `.env`:
```bash
cp .env.example .env
```
*(Kosongkan `DATABASE_URL` pada `.env` untuk menggunakan database SQLite lokal)*.

### 4. Migration & Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Jalankan Dev Server
```bash
python manage.py runserver
```

Buka peramban di:
- **Portofolio**: `http://localhost:8000/`
- **Blog**: `http://localhost:8000/blog/`
- **Admin CMS**: `http://localhost:8000/admin/`

---

## ☁️ Panduan Deployment ke Vercel & Supabase

### 1. Konfigurasi Vercel Dashboard
- Connect repository ini ke Vercel.
- Tetapkan **Root Directory** = `django`.

### 2. Set Environment Variables di Vercel Settings
Tambahkan variabel berikut pada **Settings > Environment Variables**:

| Key | Example Value | Deskripsi |
|---|---|---|
| `SECRET_KEY` | `your-production-secret-key` | Secret key unik produksi |
| `DEBUG` | `False` | Matikan mode debug |
| `ALLOWED_HOSTS` | `wisnubaldas.net,www.wisnubaldas.net,.vercel.app` | Host domain yang diizinkan |
| `CSRF_TRUSTED_ORIGINS` | `https://wisnubaldas.net,https://www.wisnubaldas.net,https://*.vercel.app` | Origin CSRF terpercaya |
| `DATABASE_URL` | `postgresql://postgres.[ref]:[password]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres` | Connection string Supabase Pooler |

### 3. Build & Deploy
Vercel akan menjalankan `buildCommand`:
```bash
python manage.py collectstatic --noinput
```
Semua request akan diarahkan ke `api/index.py` yang mengekspor WSGI Django.

---

## 📜 Lisensi & Penulis

- **Penulis**: [Wisnu Hidayat](https://www.facebook.com/Wisnubaldas)
- **Domain**: [wisnubaldas.net](https://wisnubaldas.net)
