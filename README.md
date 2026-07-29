# Blog & Portofolio Pribadi — Wisnu Hidayat

Situs web personal resmi **Wisnu Hidayat** yang terbagi menjadi dua aplikasi Django terpisah:
1. **Portofolio / Company Profile**: Domain `wisnubaldas.net` (folder `my-profile/`)
2. **Blog Utama**: Subdomain `blog.wisnubaldas.net` (folder `blog/`)

Dikembangkan menggunakan **Django 6.0**, **HTMX**, dan **SQLite (Dev) / Supabase PostgreSQL (Prod)** dengan pendekatan **MVT Murni** (Model-View-Template).

---

## 🚀 Fitur Utama

### 🏢 1. Company Profile / Portofolio (`my-profile/` — `wisnubaldas.net`)
- **One-Page Parallax UI**: Efek scroll-spy, parallax background, dan animasi responsif berbasis `one-page-parallax` theme.
- **Section Profil**: Hero Banner, Tentang Saya, Ringkasan Keahlian (Progress Bar), Pengalaman Kerja & Pendidikan, Layanan, Portofolio Proyek, dan Form Kontak.
- **Form Kontak Dynamic (HTMX)**: Pengiriman pesan instan tanpa reload halaman, tersimpan di database (`ContactMessage`).
- **CMS Admin**: Pengelolaan data profil, skill, timeline pengalaman, proyek portofolio, dan pesan masuk.

### 📝 2. Blog Teknis & Catatan (`blog/` — `blog.wisnubaldas.net`)
- **Indeks & Grid View**: Tampilan artikel publik dengan waktu baca, tanggal rilis, gambar sampul, dan pagination.
- **Live Search HTMX**: Pencarian artikel secara *real-time* berbasis keyword tanpa reload halaman.
- **Kategori & Tagging**: Filter artikel berdasarkan kategori dan tag teknis.
- **Detail Artikel Kaya Format**: Editor `django-ckeditor-5`, breadcrumb, tombol share media sosial, dan rekomendasi artikel terkait.
### 👑 3. Unified Admin Dashboard (Full CRUD)
- **Single Control Panel**: Akses Admin di `wisnubaldas.net/admin` maupun `blog.wisnubaldas.net/admin` menyajikan seluruh CRUD model database (`Profile`, `Skill`, `SocialLink`, `Experience`, `Project`, `Post`, `Category`, `Tag`, `ContactMessage`).
- **Serverless PostgreSQL Resilience**: Konfigurasi koneksi database yang dioptimalkan untuk Vercel Serverless Function (pencegahan timeout & stale SSL socket).

---

## 🛠️ Stack Teknologi

- **Backend**: Python 3.12, Django 6.0
- **Frontend Interaktivitas**: HTMX 1.9.12 (Server-Driven UI)
- **Styling & Theme**: Vanilla CSS, Bootstrap, Color Admin Parallax & Blog Themes
- **Rich Text Editor**: `django-ckeditor-5`
- **Database**:
  - Development Lokal: Shared SQLite (`db.sqlite3` di root repositori untuk `my-profile` & `blog`)
  - Production Server: Supabase PostgreSQL (Shared database via `DATABASE_URL`)
- **Static Files Storage**: WhiteNoise (`CompressedManifestStaticFilesStorage`)
- **Deployment Platform**: Vercel (Dua Vercel project terpisah berbasis `my-profile/` dan `blog/`)

---

## 📂 Struktur Proyek Terpisah

```text
blog-baldas/
├── .agents/                          # Referensi data diri & template UI
├── db.sqlite3                        # Database SQLite lokal terpadu (shared local DB)
├── my-profile/                       # Project 1: Portofolio (wisnubaldas.net)
│   ├── manage.py
│   ├── config/                       # Settings, URLs, WSGI/ASGI
│   ├── apps/company_profile/         # App Portofolio Parallax
│   ├── static/
│   ├── api/index.py                  # Entry point Vercel
│   ├── vercel.json                   # Build & rewrite Vercel
│   └── requirements.txt
├── blog/                             # Project 2: Blog (blog.wisnubaldas.net)
│   ├── manage.py
│   ├── config/                       # Settings, URLs, WSGI/ASGI
│   ├── apps/blog/                    # App Blog Mandiri
│   ├── static/
│   ├── api/index.py                  # Entry point Vercel
│   ├── vercel.json                   # Build & rewrite Vercel
│   └── requirements.txt
├── AGENTS.md                         # Kontrak agent & aturan arsitektur
└── README.md                         # Dokumentasi utama repository
```

---

## 💻 Panduan Jalankan di Lokal (Development)

### 1. Migrasi & Seeding Data Awal (Shared SQLite)
Sebelum menjalankan aplikasi, terapkan migrasi database dan masukkan data awal (*seeding*):
```bash
# Migrasi dan seed data Portofolio (company_profile)
cd my-profile
python manage.py migrate
python manage.py seed_profile

# Migrasi dan seed data Blog (blog)
cd ../blog
python manage.py migrate
python manage.py seed_blog
```

### 2. Jalankan Server Portofolio (`my-profile`)
```bash
cd my-profile
python manage.py runserver 8000
```
Buka peramban di: `http://localhost:8000/`

### 3. Jalankan Server Blog (`blog`)
Buka terminal baru:
```bash
cd blog
python manage.py runserver 8001
```
Buka peramban di: `http://localhost:8001/`

---

## 🗄️ Seeding Data ke Supabase PostgreSQL (Production)

Untuk memasok data awal ke Supabase PostgreSQL dari terminal lokal:
```bash
# 1. Seed data Portofolio ke Supabase
cd my-profile
python manage.py migrate
python manage.py seed_profile

# 2. Seed data Blog ke Supabase
cd ../blog
python manage.py migrate
python manage.py seed_blog
```
*(Pastikan `.env` memiliki `DATABASE_URL` dan `USE_POSTGRES=True` saat mengoperasikan command ini ke Supabase).*

---

## ☁️ Panduan Deployment ke Vercel

Buat **dua project terpisah** di Vercel Dashboard dari repositori yang sama:

### 1. Deployment `my-profile` (Domain: `wisnubaldas.net`)
- **Vercel Project Name**: `wisnubaldas-profile`
- **Root Directory**: `my-profile`
- **Custom Domain**: `wisnubaldas.net` (dan `www.wisnubaldas.net`)
- **Environment Variables**:
  - `SECRET_KEY`: secret key unik produksi
  - `DEBUG`: `False`
  - `ALLOWED_HOSTS`: `wisnubaldas.net,www.wisnubaldas.net,.vercel.app`
  - `CSRF_TRUSTED_ORIGINS`: `https://wisnubaldas.net,https://www.wisnubaldas.net,https://*.vercel.app`
  - `BLOG_URL`: `https://blog.wisnubaldas.net`
  - `DATABASE_URL`: Connection string PostgreSQL managed (Supabase)

### 2. Deployment `blog` (Domain: `blog.wisnubaldas.net`)
- **Vercel Project Name**: `wisnubaldas-blog`
- **Root Directory**: `blog`
- **Custom Domain**: `blog.wisnubaldas.net`
- **Environment Variables**:
  - `SECRET_KEY`: secret key unik produksi
  - `DEBUG`: `False`
  - `ALLOWED_HOSTS`: `blog.wisnubaldas.net,.vercel.app`
  - `CSRF_TRUSTED_ORIGINS`: `https://blog.wisnubaldas.net,https://*.vercel.app`
  - `MAIN_PROFILE_URL`: `https://wisnubaldas.net`
  - `DATABASE_URL`: Connection string PostgreSQL managed (Supabase)

---

## 📜 Lisensi & Penulis

- **Penulis**: [Wisnu Hidayat](https://www.facebook.com/Wisnubaldas)
- **Domain Portofolio**: [wisnubaldas.net](https://wisnubaldas.net)
- **Domain Blog**: [blog.wisnubaldas.net](https://blog.wisnubaldas.net)
