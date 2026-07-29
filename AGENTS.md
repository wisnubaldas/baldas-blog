# Instruksi Agent - Blog & Portofolio Pribadi

Dokumen ini adalah kontrak kerja untuk semua coding agent pada repository ini. Gunakan instruksi ini sebagai sumber kebenaran implementasi. Ditulis dalam Markdown standar tanpa sintaks khusus agar dapat dipakai oleh Antigravity maupun agent lain yang mendukung `AGENTS.md`.

## Tujuan produk

Bangun situs portofolio pribadi Wisnu Hidayat dengan dua pengalaman yang **terpisah secara aplikasi dan UI**:

1. **Company Profile / Portofolio** - landing page one-page dengan efek parallax, ringkasan profil, keahlian, pengalaman, proyek, dan kontak.
2. **Blog** - halaman daftar artikel, detail artikel, kategori/tag, pencarian, dan halaman statis yang menggunakan gaya blog.

Stack wajib: **Django + HTMX + SQLite**. Gunakan Django template engine dan pendekatan **MVT murni**. Jangan mengganti stack dengan React, Vue, SPA, API-first, atau CMS pihak ketiga kecuali diminta secara eksplisit.

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

Direktori `django/` adalah root aplikasi Django. Struktur targetnya:

```text
django/
├── manage.py
├── config/                         # konfigurasi proyek: settings, root URL, ASGI/WSGI
├── apps/
│   ├── company_profile/            # app portofolio/parallax
│   │   ├── migrations/
│   │   ├── templates/company_profile/
│   │   ├── static/company_profile/
│   │   ├── controllers/            # controller per menu/kelompok route
│   │   │   ├── __init__.py
│   │   │   ├── home_controller.py
│   │   │   ├── profile_controller.py
│   │   │   ├── portfolio_controller.py
│   │   │   └── contact_controller.py
│   │   ├── models/                 # model per domain; bukan satu models.py besar
│   │   │   ├── __init__.py
│   │   │   ├── profile.py
│   │   │   ├── experience.py
│   │   │   └── project.py
│   │   ├── urls/                   # route per kelompok menu
│   │   │   ├── __init__.py
│   │   │   ├── home_urls.py
│   │   │   ├── profile_urls.py
│   │   │   ├── portfolio_urls.py
│   │   │   └── contact_urls.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── services.py             # hanya jika logika domain memang diperlukan
│   └── blog/                       # app blog yang mandiri
│       ├── migrations/
│       ├── templates/blog/
│       ├── static/blog/
│       ├── controllers/
│       │   ├── __init__.py
│       │   ├── post_controller.py
│       │   ├── category_controller.py
│       │   ├── search_controller.py
│       │   └── page_controller.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── post.py
│       │   ├── category.py
│       │   └── tag.py
│       ├── urls/
│       │   ├── __init__.py
│       │   ├── post_urls.py
│       │   ├── category_urls.py
│       │   ├── search_urls.py
│       │   └── page_urls.py
│       ├── admin.py
│       ├── apps.py
│       └── services.py
├── templates/                      # base template lintas app bila diperlukan
├── static/                         # static global/vendor yang dibagi kedua app
├── media/                          # unggahan development; jangan commit hasil upload
├── api/
│   └── index.py                    # entry point Python untuk Vercel
├── vercel.json                     # konfigurasi deployment Vercel
├── db.sqlite3                      # database development lokal; jangan commit bila sudah di-ignore
└── requirements.txt
```

Nama folder `company-profile` yang tampak pada rancangan produk dipakai untuk nama/URL produk (mis. `/` atau `/company-profile/`), **bukan** nama Python package. Python package wajib memakai `company_profile` karena tanda hubung tidak dapat diimpor Django. Jangan membuat dua aplikasi paralel untuk profil dan portofolio; keduanya berada dalam app `company_profile` sampai ada kebutuhan domain yang nyata untuk dipisah.

### Struktur controller dan model per app

Setiap Django app mengikuti struktur folder ala CodeIgniter. Package `controllers/` menggantikan `views.py` konvensional Django; package `models/` menggantikan `models.py`; dan package `urls/` menggantikan `urls.py`. Jangan membuat file `views.py`, `models.py`, atau `urls.py` paralel setelah struktur package ini dipilih.

- `urls/` memecah deklarasi route bernama per menu. Setiap `*_urls.py` hanya mengimpor callable controller dan mendeklarasikan `urlpatterns`; tidak boleh memuat query, logika bisnis, atau HTML. `urls/__init__.py` wajib menggabungkan dan mengekspor satu `urlpatterns`, sehingga router utama dapat tetap memakai `include("apps.company_profile.urls")` atau `include("apps.blog.urls")`.
- Satu file di `controllers/` mewakili satu menu besar atau kelompok route yang saling berhubungan. Contoh: `portfolio_controller.py` menangani daftar dan detail portofolio; `post_controller.py` menangani indeks dan detail artikel. Tidak perlu membuat satu controller untuk route kecil yang masih bagian dari menu yang sama.
- Nama callable controller menggunakan kata kerja/konteks yang jelas, misalnya `home`, `list_projects`, `project_detail`, `post_list`, dan `post_detail`. Function-based controller adalah default.
- Controller hanya mengorkestrasi request: ambil data melalui model/service, validasi input, memilih template/partial, lalu `render()` atau `redirect()`. Controller tidak boleh memuat definisi model atau markup HTML.
- `models/` dipecah menurut entitas/domain, misalnya `models/project.py` dan `models/post.py`. Semua model aktif harus diekspor dari `models/__init__.py` supaya Django tetap dapat menemukan `app.models` dan migration/admin dapat mengimpornya konsisten.
- `templates/company_profile/` dan `templates/blog/` adalah lapisan view/presentation. Susun template berdasarkan menu: `home.html`, `profile.html`, `portfolio/list.html`, `portfolio/detail.html`, serta `partials/` untuk fragmen reusable/HTMX. Hindari folder template generik yang mencampur kedua app.
- `admin.py` mengimpor model dari package `models`, bukan menduplikasi deklarasi model. Migration Django tetap berada di `migrations/` dan selalu dihasilkan melalui perintah Django.

## Konvensi gaya CI 2, diterjemahkan ke Django MVT

Organisasi harus mudah dibaca seperti CodeIgniter 2, namun tetap idiomatik Django:

- `config/urls.py` adalah router utama seperti `routes.php`; setiap app memiliki package `urls/` sendiri, diekspos sebagai modul `app.urls`, dan diberi namespace.
- `controllers/` berfungsi sebagai controller: setiap file mewakili menu/kelompok route, menerima request, memvalidasi input ringan, memanggil model/service, lalu `render()` atau `redirect()`.
- `models/` memuat skema, relasi, query manager, dan aturan data yang dekat dengan domain; satu file per entitas/domain.
- `templates/<app_name>/` adalah view/presentation. Template hanya menangani tampilan, looping, kondisi sederhana, dan tag Django - tidak boleh menyimpan logika bisnis atau query database.
- `services.py` opsional. Buat hanya untuk alur bisnis yang tidak layak berada di view/model. Jangan membuat lapisan repository/controller/service kosong hanya demi pola.
- Gunakan function-based views untuk halaman sederhana; gunakan class-based views hanya saat mengurangi duplikasi secara nyata.
- URL harus eksplisit, bernama, dan dibuat melalui `{% url %}`/`reverse()`, bukan hard-code path di template.

## Routing dan batas aplikasi

- `company_profile` menangani `/` (home parallax), `/portfolio/`, dan halaman/detail portofolio bila diperlukan.
- `blog` menangani seluruh `/blog/`: indeks, detail berdasarkan slug, kategori/tag, pencarian, dan endpoint partial HTMX.
- Navigasi lintas aplikasi harus memakai named URL. Header dapat punya markup berbeda karena masing-masing UI memang berbeda.
- Jangan memaksa satu `base.html` tunggal jika itu mengorbankan ketepatan template parallax atau blog. Boleh gunakan `company_profile/base.html` dan `blog/base.html`; ekstrak partial hanya bila markup benar-benar sama.

## Kontrak UI

- Portofolio mengikuti bundle `one-page-parallax`: gunakan CSS `assets/css/one-page-parallax/vendor.min.css` dan `app.min.css`, serta JS `assets/js/one-page-parallax/vendor.min.js` dan `app.min.js` yang relevan.
- Blog mengikuti bundle `blog`: gunakan pasangan CSS/JS dari `assets/css/blog/` dan `assets/js/blog/`.
- Saat memindahkan asset ke Django, gunakan `{% load static %}` dan `{% static '...' %}`. Perbarui semua path gambar, CSS, JS, dan link internal dengan aman.
- Pertahankan class penting, struktur section, serta atribut plugin seperti `data-paroller`, `data-click`, `data-scroll-target`, dan `data-animation` jika elemen tersebut masih dipakai. Jangan mengganti dengan library UI lain.
- Saat data dari database dirender, masukkan ke dalam markup tema yang ada. Jangan mengubah tampilan menjadi tabel/admin-like.
- Desain harus responsif dan tetap dapat dinavigasi tanpa JavaScript. Setiap gambar konten memiliki `alt` yang bermakna; semantic heading harus berurutan.

## Django, data, dan HTMX

- SQLite adalah database development awal. Semua perubahan model harus disertai migration yang dapat dijalankan.
- Gunakan admin Django sebagai CMS awal untuk profil, proyek, artikel, kategori/tag, dan media. Lengkapi `list_display`, pencarian, filter, prepopulated slug, dan fieldset bila memberi nilai nyata.
- Model minimal blog yang diharapkan: `Post` (judul, slug unik, excerpt, body, cover image opsional, status draft/published, published_at, timestamps), `Category`, dan `Tag`. Gunakan relasi yang jelas dan ordering konsisten.
- Model portofolio dibuat berdasarkan data referensi, misalnya `Profile`, `Skill`, `Experience`, dan `Project`, hanya ketika data perlu dikelola dari admin. Jangan membangun model kosong yang belum dipakai halaman mana pun.
- Konten kaya dari admin harus disanitasi atau dirender secara aman. Jangan memakai `|safe` pada input bebas tanpa mekanisme sanitasi yang eksplisit.
- HTMX digunakan untuk peningkatan interaksi kecil dan server-rendered: pencarian/filter blog, pagination/load more, atau partial daftar proyek. Endpoint HTMX harus mengembalikan partial template saat `HX-Request` dan halaman penuh untuk request biasa bila URL itu dapat diakses langsung.
- Semua form POST memakai CSRF. Terapkan validasi server-side, pesan error yang jelas, dan redirect setelah POST sukses.
- Hindari N+1 query: gunakan `select_related`/`prefetch_related` ketika daftar menampilkan relasi.

## Konfigurasi dan kebersihan repository

- Mulai dari setting development yang aman: `DEBUG` dan `SECRET_KEY` dibaca dari environment untuk deployment; `ALLOWED_HOSTS`, static, media, locale/timezone, dan template dirs dikonfigurasi jelas.
- Jangan commit `.env`, secret, database berisi data pribadi, atau media upload. Sediakan `.env.example` tanpa nilai rahasia jika konfigurasi environment dibuat.
- Tambahkan/pertahankan `.gitignore` untuk `.venv/`, `__pycache__/`, `.env`, SQLite lokal bila dipilih, `media/`, dan file build/editor sementara.
- Pin dependensi di `requirements.txt`. Tambahkan paket hanya bila diperlukan; HTMX dapat dilayani sebagai static vendor atau CDN yang terkontrol sesuai keputusan proyek.
- Jangan mengubah berkas biner referensi di `.agents/`. Aset runtime yang dipilih harus berada di `django/static/` atau static app yang sesuai.

## Deployment Vercel

Vercel harus dikonfigurasi dengan **Root Directory = `django`** di dashboard proyek. Dengan keputusan ini, `django/` adalah root build/deployment dan seluruh path di bawah ini relatif terhadapnya. Jangan meletakkan `vercel.json` kedua di root repository kecuali Root Directory sengaja diubah dan seluruh path dikaji ulang.

Tambahkan konfigurasi berikut saat bootstrap Django:

`django/vercel.json`

```json
{
  "buildCommand": "python manage.py collectstatic --noinput",
  "rewrites": [{ "source": "/(.*)", "destination": "/api/index.py" }]
}
```

`django/api/index.py`

```python
from config.wsgi import application

app = application
```

Konvensi konfigurasi production Django:

- `requirements.txt` wajib memuat `Django`, `whitenoise`, dan semua library runtime yang benar-benar dipakai aplikasi.
- Di `settings.py`, baca `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, dan `CSRF_TRUSTED_ORIGINS` dari environment. `DEBUG` harus `False` pada Vercel.
- Tambahkan `whitenoise.middleware.WhiteNoiseMiddleware` tepat setelah `SecurityMiddleware`, tetapkan `STATIC_ROOT = BASE_DIR / "staticfiles"`, dan gunakan storage WhiteNoise bermodul manifest pada production. `collectstatic` harus berhasil sebelum deploy dianggap selesai.
- Gunakan `VERCEL_URL` bila tersedia untuk membentuk host deployment preview, tetapi production domain harus dimasukkan eksplisit ke `ALLOWED_HOSTS` dan `CSRF_TRUSTED_ORIGINS` melalui environment variable. Jangan memakai wildcard host pada production.
- Set environment variables di Vercel Dashboard untuk Production, Preview, dan Development sesuai kebutuhan: minimal `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, dan `CSRF_TRUSTED_ORIGINS`; tambahkan `DATABASE_URL` ketika database production dipakai. Nilai rahasia tidak boleh ditulis di `vercel.json`, committed `.env`, atau template.
- Semua route direwrite ke WSGI Django; file static akan dilayani oleh WhiteNoise. Pastikan URL static yang dihasilkan template memakai `{% static %}` dan tidak mengandalkan path relatif dari HTML referensi.

### Aturan database pada Vercel

SQLite hanya dipakai untuk development lokal dan demo tanpa penulisan data. Filesystem function Vercel tidak menyediakan penyimpanan database yang persisten; perubahan database SQLite saat request tidak boleh diasumsikan bertahan antardeploy atau antar-instance.

Sebelum mengaktifkan admin, publikasi artikel, form kontak tersimpan, atau fitur lain yang menulis data pada deployment Vercel, migrasikan environment production ke PostgreSQL managed dan konfigurasi koneksinya melalui `DATABASE_URL`. Tetap pertahankan SQLite sebagai default lokal jika diinginkan. Jalankan `python manage.py migrate` terhadap database production secara terkontrol pada proses release - jangan menjalankan migration secara otomatis untuk setiap request.

## Alur kerja agent

1. Sebelum mengimplementasikan halaman atau data, periksa referensi yang paling relevan di `.agents/`.
2. Buat perubahan sekecil mungkin yang menyelesaikan kebutuhan, tanpa menghapus perubahan pengguna yang tidak terkait.
3. Untuk perubahan Django: jalankan minimal `python manage.py makemigrations --check`, `python manage.py migrate`, dan `python manage.py check` dari `django/`; jalankan test yang relevan jika tersedia.
4. Untuk perubahan UI: verifikasi halaman pada viewport desktop dan mobile, pastikan asset tidak 404 dan plugin tema tidak menghasilkan error JavaScript.
5. Untuk perubahan deployment: jalankan `python manage.py collectstatic --noinput` pada konfigurasi production yang aman, lalu verifikasi preview Vercel (halaman utama, `/blog/`, static CSS/JS/gambar, admin bila diaktifkan, dan response 404/500).
6. Laporkan file yang berubah, perilaku yang dihasilkan, asumsi data yang dibuat, dan perintah verifikasi yang dijalankan.

## Definition of done

Sebuah fitur selesai bila route dapat diakses, memakai template tema yang tepat, data ditampilkan dari sumber yang tepat, responsive, aman untuk request/form yang relevan, tidak merusak aplikasi lain, dan lulus pemeriksaan Django yang sesuai. Jika informasi personal atau detail proyek tidak ditemukan pada referensi, gunakan placeholder eksplisit yang mudah diedit atau minta arahan - jangan mengarang.
