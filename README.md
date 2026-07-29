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
- **Kontak & About Me Blog**: Halaman kontak dan profil mandiri khusus konteks blog.

---

## 🛠️ Stack Teknologi

- **Backend**: Python 3.12, Django 6.0
- **Frontend Interaktivitas**: HTMX 1.9.12 (Server-Driven UI)
- **Styling & Theme**: Vanilla CSS, Bootstrap, Color Admin Parallax & Blog Themes
- **Rich Text Editor**: `django-ckeditor-5`
- **Database**:
  - Development Lokal: SQLite (`db.sqlite3` di masing-masing folder)
  - Production Server: Supabase PostgreSQL
- **Static Files Storage**: WhiteNoise (`CompressedManifestStaticFilesStorage`)
- **Deployment Platform**: Vercel (Dua Vercel project terpisah berbasis `my-profile/` dan `blog/`)

---

## 📂 Struktur Proyek Terpisah

```text
blog-baldas/
├── .agents/                          # Referensi data diri & template UI
├── my-profile/                       # Project 1: Portofolio (wisnubaldas.net)
│   ├── manage.py
│   ├── config/                       # Settings, URLs, WSGI/ASGI
│   ├── apps/company_profile/         # App Portofolio Parallax
│   ├── static/
│   ├── api/index.py                  # Entry point Vercel
│   ├── vercel.json                   # Build & rewrite Vercel
│   ├── requirements.txt
│   └── db.sqlite3
├── blog/                             # Project 2: Blog (blog.wisnubaldas.net)
│   ├── manage.py
│   ├── config/                       # Settings, URLs, WSGI/ASGI
│   ├── apps/blog/                    # App Blog Mandiri
│   ├── static/
│   ├── api/index.py                  # Entry point Vercel
│   ├── vercel.json                   # Build & rewrite Vercel
│   ├── requirements.txt
│   └── db.sqlite3
├── AGENTS.md                         # Kontrak agent & aturan arsitektur
└── README.md                         # Dokumentasi utama repository
```

---

## 💻 Panduan Jalankan di Lokal (Development)

### 1. Project Portofolio (`my-profile`)
```bash
cd my-profile
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```
Buka peramban di: `http://localhost:8000/`

### 2. Project Blog (`blog`)
Buka terminal baru:
```bash
cd blog
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
```
Buka peramban di: `http://localhost:8001/`

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
