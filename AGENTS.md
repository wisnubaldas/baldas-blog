# Instruksi Agent - Blog & Portofolio Pribadi

Dokumen ini adalah kontrak kerja untuk semua coding agent pada repository ini. Gunakan instruksi ini sebagai sumber kebenaran implementasi. Ditulis dalam Markdown standar tanpa sintaks khusus agar dapat dipakai oleh Antigravity maupun agent lain yang mendukung `AGENTS.md`.

## Tujuan produk

Bangun situs portofolio pribadi dan blog Wisnu Hidayat yang **terpisah secara aplikasi, repositori folder, dan deployment Vercel**:

1. **`my-profile` (Company Profile / Portofolio)** - Project Django mandiri untuk domain `wisnubaldas.net`. Landing page one-page dengan efek parallax, ringkasan profil, keahlian, pengalaman, proyek, dan kontak.
2. **`blog` (Blog Utama)** - Project Django mandiri untuk subdomain `blog.wisnubaldas.net`. Halaman daftar artikel, detail artikel, kategori/tag, pencarian, dan halaman statis gaya blog.

Stack wajib: **Django + HTMX + SQLite (dev) / PostgreSQL (production)**. Gunakan Django template engine dan pendekatan **MVT murni**. Jangan mengganti stack dengan React, Vue, SPA, API-first, atau CMS pihak ketiga kecuali diminta secara eksplisit.

## Referensi wajib dan batasannya

Folder `.agents/` adalah bahan referensi internal. Jangan menghapus, merombak, atau menjadikan folder tersebut sebagai lokasi runtime aplikasi.

| Referensi                                | Gunakan untuk                 | Aturan                                                                                                                                                                                            |
| ---------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.agents/template-ui/one-page-parallax/` | UI company profile/portofolio | Jadikan `index.html` sebagai acuan utama. Pertahankan struktur HTML, class CSS, data-attribute, plugin, animasi, dan perilaku parallax dari tema.                                                 |
| `.agents/template-ui/blog/`              | UI blog                       | Pilih referensi sesuai halaman: `index.html`, `post_grid.html`, `post_detail.html`, `post_without_sidebar.html`, `about_me.html`, dan `contact_us.html`. Pertahankan kontrak visualnya.           |
| `.agents/template-ui/assets/`            | Asset tema                    | Salin hanya asset yang benar-benar dibutuhkan ke static Django; jangan mengubah file sumber referensi. CSS/JS tema tetap digunakan, bukan ditulis ulang dari nol.                                 |
| `.agents/data-diri/`                     | Fakta profil pribadi          | Ekstrak dan gunakan hanya informasi yang dapat diverifikasi dari berkas ini. Jangan mengarang riwayat, sertifikasi, tautan, jabatan, atau angka.                                                  |
| `.agents/portopolio/`                    | Isi proyek terdahulu          | Jadikan screenshot/dokumen sebagai bukti dan sumber metadata proyek. Gunakan gambar dengan atribusi/keterangan yang sesuai; jangan mengklaim peran atau hasil yang tidak terlihat dari referensi. |

Jika ada perbedaan antara data pribadi dan placeholder pada template, data pribadi menang. Ganti merek, teks dummy, tautan pembelian, nama "Color Admin", dan CTA contoh dengan konten situs ini. Jangan menyertakan tautan promosi template ke situs produksi.

## Struktur proyek

Repositori ini terbagi menjadi dua project Django terpisah di bawah root:

```text
.
├── .agents/                        # Referensi internal data diri & template
├── db.sqlite3                      # Database SQLite lokal terpadu (shared local DB)
├── my-profile/                     # Project 1: Portofolio (wisnubaldas.net)
│   ├── manage.py
│   ├── config/                     # settings, urls, wsgi, asgi, context_processors
│   ├── apps/
│   │   └── company_profile/        # app portofolio/parallax
│   │       ├── migrations/
│   │       ├── templates/company_profile/
│   │       ├── static/company_profile/
│   │       ├── controllers/        # home_controller, profile_controller, dll.
│   │       ├── models/             # profile, experience, project, contact
│   │       ├── urls/               # home_urls, portfolio_urls, contact_urls
│   │       ├── management/commands/seed_profile.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       └── services.py
│   ├── static/
│   ├── media/
│   ├── api/index.py                # entry point Vercel
│   ├── vercel.json                 # konfigurasi Vercel my-profile
│   └── requirements.txt
├── blog/                           # Project 2: Blog (blog.wisnubaldas.net)
│   ├── manage.py
│   ├── config/                     # settings, urls, wsgi, asgi, context_processors
│   ├── apps/
│   │   └── blog/                   # app blog mandiri
│   │       ├── migrations/
│   │       ├── templates/blog/
│   │       ├── static/blog/
│   │       ├── controllers/        # post_controller, category_controller, search_controller, page_controller
│   │       ├── models/             # post, category, tag, contact
│   │       ├── urls/               # post_urls, category_urls, search_urls, page_urls
│   │       ├── management/commands/seed_blog.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       └── services.py
│   ├── static/
│   ├── media/
│   ├── api/index.py                # entry point Vercel
│   ├── vercel.json                 # konfigurasi Vercel blog
│   └── requirements.txt
├── README.md
└── AGENTS.md
```

### Struktur controller dan model per app

Setiap Django app dalam `my-profile` dan `blog` mengikuti struktur folder ala CodeIgniter:
- Package `controllers/` menggantikan `views.py` konvensional.
- Package `models/` dipecah per domain (`models/__init__.py` mengimpor semua model).
- Package `urls/` memecah deklarasi route (`urls/__init__.py` mengekspor `urlpatterns`).
- `templates/<app_name>/` adalah lapisan tampilan.

## Konvensi gaya CI 2, diterjemahkan ke Django MVT

- `config/urls.py` di masing-masing project adalah router utama.
- `controllers/` mengorkestrasi request, validasi input, dan memanggil render.
- Navigasi lintas domain:
  - Navigasi `my-profile` mengarah ke blog via URL variabel `BLOG_URL` (`https://blog.wisnubaldas.net`).
  - Navigasi `blog` mengarah ke portofolio via URL variabel `MAIN_PROFILE_URL` (`https://wisnubaldas.net`).

## Deployment Vercel

Kedua project di-deploy secara terpisah di Vercel:

1. **Project 1 (`my-profile`)**:
   - Vercel Dashboard **Root Directory**: `my-profile`
   - Custom Domain: `wisnubaldas.net` (dan `www.wisnubaldas.net`)
   - Environment Variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `BLOG_URL=https://blog.wisnubaldas.net`, `DATABASE_URL`

2. **Project 2 (`blog`)**:
   - Vercel Dashboard **Root Directory**: `blog`
   - Custom Domain: `blog.wisnubaldas.net`
   - Environment Variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `MAIN_PROFILE_URL=https://wisnubaldas.net`, `DATABASE_URL`

Konfigurasi `vercel.json` di masing-masing folder:
```json
{
  "buildCommand": "python manage.py collectstatic --noinput",
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/staticfiles/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

`api/index.py` di masing-masing folder:
```python
from config.wsgi import application

def app(environ, start_response):
    path_info = environ.get("PATH_INFO", "")
    if path_info.startswith("/api/index.py"):
        path_info = path_info[len("/api/index.py"):]
    elif path_info.startswith("/api/index"):
        path_info = path_info[len("/api/index"):]
    if not path_info:
        path_info = "/"
    environ["PATH_INFO"] = path_info
    environ["SCRIPT_NAME"] = ""
    return application(environ, start_response)
```

### Aturan database pada Vercel

SQLite hanya dipakai untuk development lokal. Untuk production Vercel, gunakan PostgreSQL (misalnya Supabase Managed PostgreSQL) dengan mengatur environment variable `DATABASE_URL`.

## Alur kerja agent

1. Sebelum membuat/mengubah halaman, periksa referensi `.agents/`.
2. Untuk pengujian local `my-profile`: jalankan perintah di `my-profile/` (`python manage.py check`, `python manage.py migrate`, `python manage.py seed_profile`, `python manage.py runserver 8000`).
3. Untuk pengujian local `blog`: jalankan perintah di `blog/` (`python manage.py check`, `python manage.py migrate`, `python manage.py seed_blog`, `python manage.py runserver 8001`).
4. Verifikasi `collectstatic` pada masing-masing project sebelum menyatakan fitur selesai.

## Definition of done

Sebuah fitur selesai bila route di project yang bersangkutan dapat diakses, memakai template tema yang tepat, data ditampilkan dari sumber yang tepat, responsive, aman untuk request/form yang relevan, tidak merusak aplikasi lain, dan lulus pemeriksaan Django `python manage.py check`.
