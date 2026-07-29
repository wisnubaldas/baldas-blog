"""
Django management command to seed initial Profile, Skill, SocialLink, Experience, ProjectTag, and Project data.
Usage: python manage.py seed_profile
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.company_profile.models import (
    Profile,
    Skill,
    SocialLink,
    Experience,
    Project,
    ProjectTag,
)


class Command(BaseCommand):
    help = "Seed initial profile, skills, experience, and portfolio project data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Memulai seeding data company_profile..."))

        # 1. Profile
        profile, created = Profile.objects.get_or_create(
            email="wisnu@wisnubaldas.net",
            defaults={
                "full_name": "Wisnu Hidayat",
                "tagline": "Senior Full Stack Engineer & System Architect",
                "bio": "Software Engineer berpengalaman dalam membangun aplikasi enterprise, sistem ERP, dan arsitektur web modern menggunakan Python, Django, HTMX, dan PostgreSQL.",
                "bio_detail": "Lebih dari 5 tahun berpengalaman dalam merancang dan mengimplementasikan aplikasi terintegrasi. Berfokus pada arsitektur MVT murni, efisiensi database, dan performa web yang tinggi.",
                "phone": "+62 812-3456-7890",
                "location": "Tangerang / Jakarta, Indonesia",
                "is_active": True,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Profil dibuat: {profile.full_name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Profil sudah ada: {profile.full_name}"))

        # 2. Skills
        skills_data = [
            {"name": "Python", "level": 92, "category": "technical", "icon": "fab fa-python", "order": 1},
            {"name": "Django Framework", "level": 95, "category": "technical", "icon": "fas fa-cubes", "order": 2},
            {"name": "HTMX", "level": 88, "category": "technical", "icon": "fas fa-bolt", "order": 3},
            {"name": "PostgreSQL", "level": 85, "category": "technical", "icon": "fas fa-database", "order": 4},
            {"name": "SQLite", "level": 90, "category": "technical", "icon": "fas fa-server", "order": 5},
            {"name": "JavaScript (Vanilla)", "level": 85, "category": "technical", "icon": "fab fa-js", "order": 6},
            {"name": "HTML5 / CSS3 / Sass", "level": 90, "category": "technical", "icon": "fab fa-html5", "order": 7},
            {"name": "Docker & Containers", "level": 80, "category": "tool", "icon": "fab fa-docker", "order": 8},
            {"name": "Git & GitHub Workflow", "level": 92, "category": "tool", "icon": "fab fa-github", "order": 9},
            {"name": "Vercel & Cloud Deploy", "level": 85, "category": "tool", "icon": "fas fa-cloud-upload-alt", "order": 10},
        ]
        for s in skills_data:
            Skill.objects.update_or_create(
                profile=profile,
                name=s["name"],
                defaults={
                    "level": s["level"],
                    "category": s["category"],
                    "icon": s["icon"],
                    "order": s["order"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Skills berhasil di-seed."))

        # 3. Social Links
        socials_data = [
            {"platform": "github", "url": "https://github.com/wisnubaldas", "icon_class": "fab fa-github", "order": 1},
            {"platform": "linkedin", "url": "https://linkedin.com/in/wisnubaldas", "icon_class": "fab fa-linkedin", "order": 2},
            {"platform": "website", "url": "https://wisnubaldas.net", "icon_class": "fas fa-globe", "order": 3},
        ]
        for soc in socials_data:
            SocialLink.objects.update_or_create(
                profile=profile,
                platform=soc["platform"],
                defaults={
                    "url": soc["url"],
                    "icon_class": soc["icon_class"],
                    "order": soc["order"],
                    "is_visible": True,
                },
            )
        self.stdout.write(self.style.SUCCESS("Social links berhasil di-seed."))

        # 4. Experiences
        experiences_data = [
            {
                "type": "work",
                "title": "Lead Full Stack Developer",
                "organization": "PT SEIV Indonesia",
                "location": "Tangerang, Indonesia",
                "start_date": timezone.datetime(2022, 1, 1).date(),
                "end_date": None,
                "is_current": True,
                "description": "Memimpin arsitektur dan pengembangan IDERP (Integrated Enterprise Resource Planning) untuk mendukung operasional manufaktur cat, manajemen stok, dan pelaporan keuangan real-time.",
                "order": 1,
            },
            {
                "type": "work",
                "title": "Senior Software Engineer",
                "organization": "HK Group",
                "location": "Jakarta, Indonesia",
                "start_date": timezone.datetime(2020, 3, 1).date(),
                "end_date": timezone.datetime(2021, 12, 31).date(),
                "is_current": False,
                "description": "Pengembangan layanan backend terintegrasi, optimasi database PostgreSQL, dan implementasi CI/CD pipeline untuk aplikasi berskala besar.",
                "order": 2,
            },
            {
                "type": "education",
                "title": "Sarjana Komputer (S.Kom) - Teknik Informatika",
                "organization": "Universitas Pamulang",
                "location": "Tangerang Selatan, Indonesia",
                "start_date": timezone.datetime(2016, 9, 1).date(),
                "end_date": timezone.datetime(2020, 8, 31).date(),
                "is_current": False,
                "description": "Lulus dengan fokus studi Rekayasa Perangkat Lunak dan Pengolahan Data.",
                "order": 3,
            },
        ]
        for exp in experiences_data:
            Experience.objects.update_or_create(
                profile=profile,
                title=exp["title"],
                organization=exp["organization"],
                defaults=exp,
            )
        self.stdout.write(self.style.SUCCESS("Experiences berhasil di-seed."))

        # 5. Project Tags
        tags_data = [
            {"name": "Python", "slug": "python", "color": "#3776AB"},
            {"name": "Django", "slug": "django", "color": "#092E20"},
            {"name": "HTMX", "slug": "htmx", "color": "#336699"},
            {"name": "PostgreSQL", "slug": "postgresql", "color": "#4169E1"},
            {"name": "Docker", "slug": "docker", "color": "#2496ED"},
            {"name": "ERP", "slug": "erp", "color": "#E34F26"},
        ]
        tag_objs = {}
        for t in tags_data:
            obj, _ = ProjectTag.objects.update_or_create(
                slug=t["slug"],
                defaults={"name": t["name"], "color": t["color"]},
            )
            tag_objs[t["slug"]] = obj
        self.stdout.write(self.style.SUCCESS("Project tags berhasil di-seed."))

        # 6. Projects
        projects_data = [
            {
                "title": "IDERP - Integrated Enterprise Resource Planning",
                "slug": "iderp-seiv-indonesia",
                "client": "PT SEIV Indonesia",
                "short_description": "Sistem ERP terpadu untuk pengelolaan manufaktur, persediaan, dan modul akuntansi.",
                "description": "IDERP adalah solusi ERP terintegrasi yang dirancang khusus untuk memfasilitasi alur kerja pabrik manufaktur cat, memantau pergerakan bahan baku, modul penjualan, pembelian, hingga laporan keuangan otomatis.",
                "role": "Lead Architect & Full Stack Developer",
                "status": "completed",
                "year": 2023,
                "url": "https://wisnubaldas.net",
                "is_featured": True,
                "order": 1,
                "tag_slugs": ["python", "django", "postgresql", "erp"],
            },
            {
                "title": "TPS - Third Party Logistics Management",
                "slug": "tps-logistics-system",
                "client": "Logistics Enterprise",
                "short_description": "Platform manajemen armada dan pelacakan pengiriman barang secara real-time.",
                "description": "Sistem aplikasi web untuk mengelola jadwal armada pengiriman, pengalokasian driver, serta pelacakan pengiriman logistik dengan Dasbor analitik.",
                "role": "Senior Full Stack Engineer",
                "status": "completed",
                "year": 2024,
                "url": "https://wisnubaldas.net",
                "is_featured": True,
                "order": 2,
                "tag_slugs": ["python", "django", "htmx", "postgresql"],
            },
            {
                "title": "Wisnu Baldas Blog & Portfolio Platform",
                "slug": "wisnu-baldas-platform",
                "client": "Personal Project",
                "short_description": "Portofolio interaktif dan platform blog modern berbasis Django MVT & HTMX.",
                "description": "Pengembangan situs web terpisah antara domain portofolio (wisnubaldas.net) dan blog (blog.wisnubaldas.net) yang dideploy di Vercel dengan dukungan database PostgreSQL/SQLite.",
                "role": "Creator & Engineer",
                "status": "maintained",
                "year": 2026,
                "url": "https://wisnubaldas.net",
                "is_featured": True,
                "order": 3,
                "tag_slugs": ["python", "django", "htmx", "docker"],
            },
        ]

        for p_data in projects_data:
            tag_slugs = p_data.pop("tag_slugs")
            proj, _ = Project.objects.update_or_create(
                profile=profile,
                slug=p_data["slug"],
                defaults=p_data,
            )
            proj.tags.set([tag_objs[ts] for ts in tag_slugs if ts in tag_objs])
        self.stdout.write(self.style.SUCCESS("Projects berhasil di-seed."))

        self.stdout.write(self.style.SUCCESS("Seeding company_profile SELESAI."))
