# Analisis Project: Blog & Portofolio Pribadi Wisnu Hidayat

## Ringkasan Eksekutif

Project ini adalah situs web personal **Wisnu Hidayat** yang dibangun dengan **Django + HTMX + SQLite**, terdiri dari dua bagian aplikasi yang terpisah: **Company Profile / Portofolio** (one-page parallax) dan **Blog** (multi-page).

---

## Status Repository Saat Ini

> [!CAUTION]
> Repository baru diinisialisasi. **Belum ada folder `django/`** (root aplikasi Django) sama sekali. Semua yang ada saat ini:

| Item         | Keterangan                                                 |
| ------------ | ---------------------------------------------------------- |
| `.agents/`   | Referensi internal (data diri, template UI, portofolio) ✅ |
| `.gitignore` | Ada tapi sangat minimal                                    |
| `AGENTS.md`  | Instruksi agent lengkap ✅                                 |
| `README.md`  | Ada                                                        |
| `django/`    | ❌ **BELUM ADA** — perlu dibuat dari awal                  |

---

## Bahan Referensi yang Tersedia

### 1. Data Diri (`.agents/data-diri/`)

| File                                      | Keterangan           |
| ----------------------------------------- | -------------------- |
| `Wisnu_Hidayat_CV_2026_Modern.pdf`        | CV terbaru (utama)   |
| `Wisnu_Hidayat_CV_2025.pdf`               | CV 2025              |
| `Form Daftar Riwayat Hidup HK GROUP.docx` | Riwayat hidup detail |
| `Sertifikat_ijazah-1.pdf`                 | Sertifikat/Ijazah    |

### 2. Template UI (`.agents/template-ui/`)

| Folder               | Template yang Tersedia                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `one-page-parallax/` | `index.html`, `index_default_header.html`, `index_inverse_header.html`, `extra_element.html`                                                     |
| `blog/`              | `index.html`, `post_grid.html`, `post_detail.html`, `post_without_sidebar.html`, `about_me.html`, `contact_us.html`, `carousel-post_detail.html` |
| `assets/`            | `css/`, `js/`, `img/`, `plugins/`                                                                                                                |

### 3. Portofolio (`.agents/portopolio/`)

| Item                                  | Keterangan                |
| ------------------------------------- | ------------------------- |
| `Screenshoot Portopolio PT SEIV.docx` | Screenshot proyek PT SEIV |
| `iderp/`                              | Folder proyek iDERP       |
| `tps/`                                | Folder proyek TPS         |

---

## Arsitektur Target

```
blog-baldas/
└── django/                          ← ROOT APLIKASI (belum ada)
    ├── manage.py
    ├── config/                      ← settings, root URL, ASGI/WSGI
    ├── apps/
    │   ├── company_profile/         ← App portofolio (one-page parallax)
    │   │   ├── controllers/         ← Gantikan views.py
    │   │   ├── models/              ← Satu file per entitas
    │   │   └── urls/                ← Route per menu
    │   └── blog/                    ← App blog (mandiri)
    │       ├── controllers/
    │       ├── models/
    │       └── urls/
    ├── templates/                   ← Base template lintas app
    ├── static/                      ← Vendor/global static
    ├── media/                       ← Upload development
    ├── api/index.py                 ← Entry point Vercel
    ├── vercel.json
    ├── db.sqlite3
    └── requirements.txt
```

---

## Rencana Implementasi Bertahap

### 🔴 Fase 1 — Bootstrap Django (Prioritas Tertinggi)

- [ ] Buat struktur folder `django/` sesuai AGENTS.md
- [ ] Setup `config/settings.py` (dev + production-ready)
- [ ] Setup `requirements.txt` (Django, HTMX, whitenoise, dll)
- [ ] Buat `vercel.json` dan `api/index.py`
- [ ] Perbarui `.gitignore`

### 🟠 Fase 2 — App `company_profile` (Portofolio)

- [ ] Buat struktur package: `controllers/`, `models/`, `urls/`
- [ ] Ekstrak data pribadi dari CV/data-diri ke model DB
- [ ] Model: `Profile`, `Skill`, `Experience`, `Project`
- [ ] Salin aset dari `.agents/template-ui/` ke `static/`
- [ ] Implementasi template Django dari `one-page-parallax/index.html`
- [ ] Setup admin untuk kelola konten portofolio

### 🟡 Fase 3 — App `blog`

- [ ] Buat struktur package: `controllers/`, `models/`, `urls/`
- [ ] Model: `Post`, `Category`, `Tag`
- [ ] Implementasi template dari `blog/index.html`, `post_detail.html`, dll.
- [ ] Integrasi HTMX untuk: pencarian, filter, load-more
- [ ] Setup admin blog (list_display, pencarian, filter, slug)

### 🟢 Fase 4 — Polish & Deployment

- [ ] `collectstatic` + konfigurasi WhiteNoise
- [ ] Verifikasi Vercel deployment
- [ ] SEO & semantik HTML
- [ ] Uji responsivitas desktop + mobile

---

## Keputusan Teknis Penting

| Aspek                 | Keputusan                                                    |
| --------------------- | ------------------------------------------------------------ |
| **Stack**             | Django + HTMX + SQLite (dev)                                 |
| **Templating**        | Django MVT murni — bukan SPA/API                             |
| **CSS/JS**            | Gunakan bundle tema yang ada, bukan tulis ulang              |
| **Package structure** | `controllers/` bukan `views.py`, `models/` bukan `models.py` |
| **Database**          | SQLite untuk dev; PostgreSQL untuk production Vercel         |
| **Static**            | WhiteNoise untuk production                                  |
| **Deployment**        | Vercel dengan Root Directory = `django/`                     |

---

## Risiko & Hal yang Perlu Diperhatikan

> [!WARNING]
> **SQLite tidak persisten di Vercel** — Jangan aktifkan fitur tulis data (admin publish, kontak form simpan) di production sebelum migrasi ke PostgreSQL.

> [!IMPORTANT]
> **Jangan ubah file di `.agents/`** — Folder ini adalah referensi read-only. Aset runtime disalin ke `django/static/`.

> [!NOTE]
> **Data diri harus diverifikasi dari referensi** — Jangan mengarang riwayat, jabatan, atau sertifikasi. Gunakan placeholder eksplisit jika data tidak ditemukan.

> [!CAUTION]
> **Jangan gunakan `|safe` tanpa sanitasi** pada input bebas dari admin (rich text editor). Implementasikan sanitasi yang tepat.

---

## Urutan Langkah Pertama yang Disarankan

1. **Baca CV** → Ekstrak data pribadi (nama, profesi, skill, pengalaman, kontak)
2. **Bootstrap Django** → Buat `django/` dengan semua struktur yang diwajibkan
3. **Implementasi Company Profile** → Halaman utama dengan parallax
4. **Implementasi Blog** → Artikel, kategori, pencarian
5. **Deploy Vercel** → Konfigurasi environment, collectstatic, verify

---

## Pertanyaan Klarifikasi (Opsional)

Sebelum mulai implementasi, ada beberapa hal yang perlu dikonfirmasi:

1. **Rich text editor** untuk body artikel blog — pakai `django-ckeditor`, `django-quill`, atau plain `<textarea>`?
2. **Kontak form** — apakah perlu disimpan ke DB atau hanya kirim email?
3. **Domain production** — sudah ada domain custom atau pakai subdomain Vercel?
4. **Foto profil** — ada di antara file referensi atau perlu disiapkan sendiri?
