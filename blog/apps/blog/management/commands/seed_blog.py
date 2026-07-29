"""
Django management command to seed initial Category, Tag, and Post data for the blog app.
Usage: python manage.py seed_blog
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.blog.models import Category, Tag, Post


class Command(BaseCommand):
    help = "Seed initial blog categories, tags, and articles."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Memulai seeding data blog..."))

        # 1. Categories
        categories_data = [
            {
                "name": "Web Development",
                "slug": "web-development",
                "description": "Artikel seputar arsitektur web modern, frontend, dan praktik terbaik rekayasa perangkat lunak.",
                "color": "#3B82F6",
                "order": 1,
            },
            {
                "name": "Django & Python",
                "slug": "django-python",
                "description": "Tips, trik, dan panduan mendalam seputar framework Django dan bahasa pemrograman Python.",
                "color": "#10B981",
                "order": 2,
            },
            {
                "name": "System Architecture",
                "slug": "system-architecture",
                "description": "Studi kasus perancangan sistem enterprise, database, dan infrastruktur cloud.",
                "color": "#8B5CF6",
                "order": 3,
            },
            {
                "name": "Career & Engineering",
                "slug": "career-engineering",
                "description": "Pengalaman karir, kepemimpinan tim teknis, dan manajemen proyek software.",
                "color": "#F59E0B",
                "order": 4,
            },
        ]

        cat_objs = {}
        for c in categories_data:
            obj, _ = Category.objects.update_or_create(
                slug=c["slug"],
                defaults=c,
            )
            cat_objs[c["slug"]] = obj
        self.stdout.write(self.style.SUCCESS("Categories berhasil di-seed."))

        # 2. Tags
        tags_data = [
            {"name": "Django", "slug": "django"},
            {"name": "Python", "slug": "python"},
            {"name": "HTMX", "slug": "htmx"},
            {"name": "PostgreSQL", "slug": "postgresql"},
            {"name": "SQLite", "slug": "sqlite"},
            {"name": "Vercel", "slug": "vercel"},
            {"name": "Web Performance", "slug": "web-performance"},
        ]

        tag_objs = {}
        for t in tags_data:
            obj, _ = Tag.objects.update_or_create(
                slug=t["slug"],
                defaults={"name": t["name"]},
            )
            tag_objs[t["slug"]] = obj
        self.stdout.write(self.style.SUCCESS("Tags berhasil di-seed."))

        # 3. Posts
        now = timezone.now()
        posts_data = [
            {
                "title": "Membuat Web Portofolio & Blog Terpisah dengan Django + HTMX",
                "slug": "membuat-web-portofolio-blog-terpisah-django-htmx",
                "excerpt": "Panduan arsitektur memisahkan aplikasi portofolio utama dan blog menggunakan Django MVT, HTMX, serta deployment terpisah di Vercel.",
                "body": """
<p>Memisahkan situs portofolio utama dan blog ke dalam subdomain terpisah adalah praktik terbaik untuk menjaga kerapian kode dan modularitas aplikasi. Dalam artikel ini, kita akan membahas bagaimana merancang arsitektur dua project Django terpisah yang mengandalkan satu database terpadu.</p>
<h3>Mengapa Menggunakan Arsitektur MVT murni + HTMX?</h3>
<p>Banyak pengembang terjebak menggunakan SPA (Single Page Application) seperti React atau Vue untuk situs pribadi sederhana, yang seringkali menambah kompleksitas build step dan pembengkakan bundle JS. Dengan Django MVT dan HTMX, kita memperoleh kemudahan render server-side sekaligus interaktivitas dinamis ala SPA.</p>
<ul>
  <li><b>MVT Murni:</b> Routing dan render template diproses langsung oleh Django.</li>
  <li><b>HTMX:</b> Mengganti komponen halaman secara parsial tanpa reload penuh.</li>
  <li><b>Pengelolaan Asset:</b> WhiteNoise menangani kompresi dan hashing berkas statis secara efisien di produksi.</li>
</ul>
<p>Dengan pendekatan ini, performa loading situs menjadi jauh lebih cepat dan ramah SEO.</p>
""",
                "category_slug": "django-python",
                "tag_slugs": ["django", "python", "htmx", "vercel"],
                "status": "published",
                "published_at": now,
            },
            {
                "title": "Mengapa HTMX dan Django Adalah Kombinasi Sempurna untuk Solo Developer",
                "slug": "mengapa-htmx-dan-django-kombinasi-sempurna-solo-developer",
                "excerpt": "Bagaimana HTMX memberikan pengalaman SPA yang responsif tanpa perlu kerumitan React/Vue build step bagi pengembang mandiri.",
                "body": """
<p>Sebagai seorang pengembang software mandiri, efisiensi waktu dan kemudahan pemeliharaan kode adalah prioritas utama. HTMX memberikan paradigma baru dalam pengembangan web modern.</p>
<h3>Kelebihan Utama HTMX:</h3>
<ol>
  <li><b>Tanpa JavaScript Build Tools:</b> Tidak memerlukan npm, webpack, atau vite untuk mengelola tampilan dinamis.</li>
  <li><b>Akses HTTP Langsung dari HTML:</b> Anda dapat mengirimkan request GET, POST, PUT, DELETE langsung dari atribut HTML seperti <code>hx-get</code> dan <code>hx-target</code>.</li>
  <li><b>Integrasi Native dengan Django Templates:</b> Partial template Django (menggunakan <code>render_to_string</code> atau HTMX response) dapat disisipkan langsung ke DOM.</li>
</ol>
<p>Kombinasi ini memangkas waktu pengembangan hingga 50% dibandingkan pendekatan REST API + Frontend Framework terpisah.</p>
""",
                "category_slug": "web-development",
                "tag_slugs": ["htmx", "django", "web-performance"],
                "status": "published",
                "published_at": now,
            },
            {
                "title": "Optimasi Database: Satu Database Terpadu untuk SQLite dan PostgreSQL",
                "slug": "optimasi-database-satu-database-terpadu-sqlite-postgresql",
                "excerpt": "Strategi mengelola satu database terpadu untuk lingkungan pengujian lokal SQLite dan produksi PostgreSQL pada Supabase.",
                "body": """
<p>Dalam pengujian lokal, menggunakan SQLite sangat praktis karena tidak membutuhkan proses server terpisah. Namun di lingkungan produksi Vercel, PostgreSQL (seperti Supabase) menjadi pilihan utama karena kapabilitas persistensi dan efisiensinya.</p>
<p>Dengan konfigurasi Django <code>dj_database_url</code>, kita dapat secara otomatis mendeteksi environment variable <code>DATABASE_URL</code> untuk switching transparan antara SQLite lokal dan PostgreSQL produksi tanpa mengubah kode aplikasi.</p>
""",
                "category_slug": "system-architecture",
                "tag_slugs": ["sqlite", "postgresql", "django"],
                "status": "published",
                "published_at": now,
            },
        ]

        for p_data in posts_data:
            cat_slug = p_data.pop("category_slug")
            tag_slugs = p_data.pop("tag_slugs")
            p_data["category"] = cat_objs.get(cat_slug)

            post_obj, _ = Post.objects.update_or_create(
                slug=p_data["slug"],
                defaults=p_data,
            )
            post_obj.tags.set([tag_objs[ts] for ts in tag_slugs if ts in tag_objs])

        self.stdout.write(self.style.SUCCESS("Posts berhasil di-seed."))
        self.stdout.write(self.style.SUCCESS("Seeding blog SELESAI."))
