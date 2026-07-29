"""
Django management command to seed Profile, Skill, SocialLink, Experience, ProjectTag, Project, and ProjectImage data.
Generated automatically from current database state.
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
    ProjectImage,
)


class Command(BaseCommand):
    help = "Seed initial profile, skills, experience, and portfolio project data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Memulai seeding data company_profile..."))

        # 1. Profile
        profile, created = Profile.objects.update_or_create(
            email='wisnu@wisnubaldas.net',
            defaults={
                "full_name": 'Wisnu Hidayat',
                "tagline": 'Programer Gadungan',
                "bio": 'Software Engineer berpengalaman dalam membangun aplikasi enterprise, sistem ERP, dan arsitektur web modern menggunakan Python, Django, HTMX, dan PostgreSQL.',
                "bio_detail": 'Lebih dari 5 tahun berpengalaman dalam merancang dan mengimplementasikan aplikasi terintegrasi. Berfokus pada arsitektur MVT murni, efisiensi database, dan performa web yang tinggi.',
                "phone": '+62 812-3456-7890',
                "location": 'Tangerang / Jakarta, Indonesia',
                "photo": 'profile/452479322_10223147159299982_3345301148279511699_n.jpg',
                "resume_file": 'resume/Wisnu_Hidayat_CV_2026_Modern.pdf',
                "is_active": True,
            },
        )
        self.stdout.write(self.style.SUCCESS(f"Profil disiapkan: {profile.full_name}"))

        # 2. Skills
        skills_data = [
            {"name": 'FastApi', "level": 80, "category": 'technical', "icon": 'fab fa-python', "order": 0},
            {"name": 'React JS', "level": 80, "category": 'technical', "icon": 'fab fa-react', "order": 0},
            {"name": 'Python', "level": 92, "category": 'technical', "icon": 'fab fa-python', "order": 1},
            {"name": 'Python (FastAPI / Django)', "level": 95, "category": 'technical', "icon": 'fab fa-python', "order": 1},
            {"name": 'Django Framework', "level": 95, "category": 'technical', "icon": 'fas fa-cubes', "order": 2},
            {"name": 'PHP (Laravel / Lumen)', "level": 95, "category": 'technical', "icon": 'fab fa-php', "order": 2},
            {"name": 'Database Design (PostgreSQL/MySQL/Redis)', "level": 92, "category": 'technical', "icon": 'fas fa-database', "order": 3},
            {"name": 'HTMX', "level": 88, "category": 'technical', "icon": 'fas fa-bolt', "order": 3},
            {"name": 'PostgreSQL', "level": 85, "category": 'technical', "icon": 'fas fa-database', "order": 4},
            {"name": 'REST API & System Integration', "level": 94, "category": 'technical', "icon": 'fas fa-network-wired', "order": 4},
            {"name": 'Frontend (Astro / React / HTMX)', "level": 88, "category": 'technical', "icon": 'fab fa-react', "order": 5},
            {"name": 'SQLite', "level": 90, "category": 'technical', "icon": 'fas fa-server', "order": 5},
            {"name": 'JavaScript (Vanilla)', "level": 85, "category": 'technical', "icon": 'fab fa-js', "order": 6},
            {"name": 'WMS & Logistics Systems', "level": 95, "category": 'technical', "icon": 'fas fa-boxes', "order": 6},
            {"name": 'Docker & Kubernetes', "level": 85, "category": 'tool', "icon": 'fab fa-docker', "order": 7},
            {"name": 'HTML5 / CSS3 / Sass', "level": 90, "category": 'technical', "icon": 'fab fa-html5', "order": 7},
            {"name": 'Docker & Containers', "level": 80, "category": 'tool', "icon": 'fab fa-docker', "order": 8},
            {"name": 'Huawei Cloud & DevOps (GitLab CI/CD)', "level": 85, "category": 'tool', "icon": 'fas fa-cloud', "order": 8},
            {"name": 'Git & GitHub Workflow', "level": 92, "category": 'tool', "icon": 'fab fa-github', "order": 9},
            {"name": 'Linux Infrastructure & Servers', "level": 90, "category": 'tool', "icon": 'fab fa-linux', "order": 9},
            {"name": 'Hardware Device Integration', "level": 88, "category": 'tool', "icon": 'fas fa-microchip', "order": 10},
            {"name": 'Vercel & Cloud Deploy', "level": 85, "category": 'tool', "icon": 'fas fa-cloud-upload-alt', "order": 10},
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
            {"platform": 'github', "url": 'https://github.com/wisnubaldas', "icon_class": 'fab fa-github', "order": 1, "is_visible": True},
            {"platform": 'github', "url": 'https://github.com/wisnubaldas', "icon_class": 'fab fa-github', "order": 1, "is_visible": True},
            {"platform": 'linkedin', "url": 'https://linkedin.com/in/wisnubaldas', "icon_class": 'fab fa-linkedin', "order": 2, "is_visible": True},
            {"platform": 'linkedin', "url": 'https://linkedin.com/in/wisnu-hidayat-64923559', "icon_class": 'fab fa-linkedin', "order": 2, "is_visible": True},
            {"platform": 'website', "url": 'https://wisnubaldas.net', "icon_class": 'fas fa-globe', "order": 3, "is_visible": True},
            {"platform": 'website', "url": 'https://wisnubaldas.net', "icon_class": 'fas fa-globe', "order": 3, "is_visible": True},
        ]
        for soc in socials_data:
            SocialLink.objects.update_or_create(
                profile=profile,
                platform=soc["platform"],
                defaults={
                    "url": soc["url"],
                    "icon_class": soc["icon_class"],
                    "order": soc["order"],
                    "is_visible": soc["is_visible"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Social links berhasil di-seed."))

        # 4. Experiences
        Experience.objects.filter(profile=profile).delete()
        Experience.objects.create(
            profile=profile,
            type='work',
            title='Full Stack Engineer',
            organization='PT Anugerah Tangkas Transportindo',
            location='Jakarta, Indonesia',
            start_date=timezone.datetime(2023, 1, 1).date(),
            end_date=timezone.datetime(2026, 6, 30).date(),
            is_current=False,
            description='Mengembangkan dan meningkatkan aplikasi manajemen logistik, kargo, dan Warehouse Management System (WMS). Merancang layanan backend menggunakan Laravel dan FastAPI, arsitektur database enterprise, serta integrasi REST API. Bekerja erat dengan tim operasional untuk digitalisasi proses bisnis logistik.',
            order=1,
        )
        Experience.objects.create(
            profile=profile,
            type='work',
            title='Full Stack Engineer',
            organization='PT Himalaya Indo Karya',
            location='Jakarta, Indonesia',
            start_date=timezone.datetime(2021, 1, 1).date(),
            end_date=timezone.datetime(2023, 12, 31).date(),
            is_current=False,
            description='Mengembangkan aplikasi web enterprise. Membangun Smart Lock System yang terintegrasi dengan perangkat Kerong Smart Lock. Mengembangkan Passport Printing System untuk operasional Imigrasi dan Kedutaan. Mengintegrasikan perangkat lunak dengan perangkat keras dan REST API serta menangani penggelaran (deployment), pemeliharaan, dan dukungan sistem produksi.',
            order=2,
        )
        Experience.objects.create(
            profile=profile,
            type='work',
            title='Software Developer',
            organization='PT Chang Jui Fang Indonesia',
            location='Indonesia',
            start_date=timezone.datetime(2019, 1, 1).date(),
            end_date=timezone.datetime(2021, 12, 31).date(),
            is_current=False,
            description='Mengembangkan dan memelihara aplikasi web enterprise manufaktur. Mengimplementasikan fitur bisnis baru, optimasi performa sistem, testing, debugging, serta memberikan dukungan teknis produksi.',
            order=3,
        )
        Experience.objects.create(
            profile=profile,
            type='work',
            title='Software Developer / IT Infrastructure',
            organization='PT Anugerah Tangkas Transportindo',
            location='Jakarta, Indonesia',
            start_date=timezone.datetime(2013, 1, 1).date(),
            end_date=timezone.datetime(2019, 12, 31).date(),
            is_current=False,
            description='Mengembangkan aplikasi logistik internal. Mengelola server Windows/Linux dan infrastruktur jaringan. Mengimplementasikan keamanan informasi, sistem cadangan (backup), otomatisasi, serta dukungan pengguna IT.',
            order=4,
        )
        Experience.objects.create(
            profile=profile,
            type='education',
            title='Sarjana Sistem Informasi (S.Kom)',
            organization='Universitas Raharja',
            location='Tangerang / Jakarta, Indonesia',
            start_date=timezone.datetime(2010, 9, 1).date(),
            end_date=timezone.datetime(2014, 8, 31).date(),
            is_current=False,
            description='Gelar Sarjana Sistem Informasi (Bachelor Degree - Information Systems) dengan fokus pada Rekayasa Perangkat Lunak, Arsitektur Sistem Informasi Enterprise, dan Manajemen Database.',
            order=5,
        )
        self.stdout.write(self.style.SUCCESS("Experiences berhasil di-seed."))

        # 5. Project Tags
        tags_data = [
            {"name": 'Codeigniter', "slug": 'codeigniter', "color": '#6c757d'},
            {"name": 'Django', "slug": 'django', "color": '#092E20'},
            {"name": 'Docker', "slug": 'docker', "color": '#2496ED'},
            {"name": 'ERP', "slug": 'erp', "color": '#E34F26'},
            {"name": 'FastAPI', "slug": 'fastapi', "color": '#009688'},
            {"name": 'HTMX', "slug": 'htmx', "color": '#336699'},
            {"name": 'Hardware Integration', "slug": 'hardware', "color": '#6f42c1'},
            {"name": 'Laravel', "slug": 'laravel', "color": '#FF2D20'},
            {"name": 'PostgreSQL', "slug": 'postgresql', "color": '#4169E1'},
            {"name": 'Python', "slug": 'python', "color": '#3776AB'},
            {"name": 'React Js', "slug": 'React', "color": '#6c757d'},
            {"name": 'WMS & Logistics', "slug": 'logistics', "color": '#E34F26'},
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
        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='tps-online',
            defaults={
                "title": 'TPS Online',
                "client": 'MAU',
                "short_description": 'Tps Online Mitra Adira Utama',
                "description": '',
                "cover_image": 'projects/covers/tps2.png',
                "role": 'Fullstack Developer',
                "status": 'completed',
                "year": 2021,
                "url": '',
                "is_featured": False,
                "is_visible": True,
                "order": 0,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['codeigniter'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='warehouse-management-system',
            defaults={
                "title": 'Warehouse Management System (WMS)',
                "client": 'PT Anugerah Tangkas Transportindo',
                "short_description": 'Sistem manajemen pergudangan enterprise untuk otomatisasi stok, inbound, outbound, dan tracking barang kargo.',
                "description": 'Pengembangan aplikasi Warehouse Management System (WMS) yang memfasilitasi penerimaan barang, tata letak ruang simpan, pelacakan stok secara akurat, integrasi scanner barcode, serta otomatisasi laporan inventaris kargo.',
                "cover_image": '',
                "role": 'Full Stack Engineer & Database Architect',
                "status": 'completed',
                "year": 2024,
                "url": 'https://wisnubaldas.net',
                "is_featured": True,
                "is_visible": True,
                "order": 1,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['fastapi', 'laravel', 'postgresql', 'logistics'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='iderp-web-version',
            defaults={
                "title": 'IDERP Web Version',
                "client": 'CJFI',
                "short_description": 'Aplikasi ERP yang di kembangkan dari PT CJFI',
                "description": 'Aplikasi ERP pengembangan dari sistem yang lama menjadi web base',
                "cover_image": '',
                "role": 'Fullstack Developer',
                "status": 'completed',
                "year": 2020,
                "url": '',
                "is_featured": False,
                "is_visible": True,
                "order": 1,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['codeigniter', 'laravel'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='cargo-logistics-system',
            defaults={
                "title": 'Cargo & Logistics Management System',
                "client": 'PT Anugerah Tangkas Transportindo',
                "short_description": 'Platform manajemen pengiriman kargo, penjadwalan armada, dan integrasi API logistik.',
                "description": 'Sistem informasi logistik terpadu untuk digitalisasi alur kerja pengiriman barang, manifesto kargo, penjadwalan pengiriman, serta pemantauan status ekspedisi secara real-time.',
                "cover_image": '',
                "role": 'Full Stack Engineer',
                "status": 'completed',
                "year": 2025,
                "url": 'https://wisnubaldas.net',
                "is_featured": True,
                "is_visible": True,
                "order": 2,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['fastapi', 'laravel', 'python', 'logistics'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='smart-lock-kerong-integration',
            defaults={
                "title": 'Smart Lock System Integration (Kerong)',
                "client": 'PT Himalaya Indo Karya',
                "short_description": 'Aplikasi kontrol akses pintar berbasis IoT terintegrasi dengan perangkat Kerong Smart Lock.',
                "description": 'Pengembangan platform manajemen akses keamanan yang menghubungkan perangkat lunak web dengan perangkat keras Kerong Smart Lock melalui REST API dan protokol enkripsi perangkat.',
                "cover_image": '',
                "role": 'Full Stack Engineer & Hardware Integrator',
                "status": 'completed',
                "year": 2022,
                "url": 'https://wisnubaldas.net',
                "is_featured": True,
                "is_visible": True,
                "order": 3,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['hardware', 'laravel', 'postgresql'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='passport-printing-system',
            defaults={
                "title": 'Passport Printing System',
                "client": 'Imigrasi & Kedutaan (PT Himalaya Indo Karya)',
                "short_description": 'Sistem pencetakan dokumen paspor dan validasi data identitas resmi imigrasi.',
                "description": 'Sistem aplikasi enterprise berkeamanan tinggi yang memproses antrean pencetakan paspor, integrasi pencetak dokumen fisik khusus, serta sinkronisasi data dengan sistem imigrasi.',
                "cover_image": '',
                "role": 'Full Stack Engineer',
                "status": 'completed',
                "year": 2023,
                "url": 'https://wisnubaldas.net',
                "is_featured": True,
                "is_visible": True,
                "order": 4,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['hardware', 'laravel', 'postgresql'] if ts in tag_objs])

        proj, _ = Project.objects.update_or_create(
            profile=profile,
            slug='wisnu-baldas-platform',
            defaults={
                "title": 'Wisnu Baldas Platform & ERP Architecture',
                "client": 'Personal / Enterprise Project',
                "short_description": 'Portofolio interaktif dan platform blog modern berbasis Django MVT & HTMX.',
                "description": 'Pengembangan situs web terpisah antara domain portofolio (wisnubaldas.net) dan blog (blog.wisnubaldas.net) yang dideploy di Vercel dengan dukungan database PostgreSQL/SQLite.',
                "cover_image": '',
                "role": 'Creator & Solution Architect',
                "status": 'maintained',
                "year": 2026,
                "url": 'https://wisnubaldas.net',
                "is_featured": True,
                "is_visible": True,
                "order": 5,
            },
        )
        proj.tags.set([tag_objs[ts] for ts in ['django', 'docker', 'htmx', 'python'] if ts in tag_objs])

        self.stdout.write(self.style.SUCCESS("Projects berhasil di-seed."))

        # 7. Project Images
        images_data = [
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp1.png', "caption": 'Landing Page', "order": 0},
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp2.png', "caption": 'Login Page', "order": 0},
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp3.png', "caption": 'Dashboard', "order": 0},
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp4.png', "caption": 'HRD Calender', "order": 0},
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp5.png', "caption": 'Ranking Penjualan Depo', "order": 0},
            {"project_slug": 'iderp-web-version', "image": 'projects/gallery/iderp7.png', "caption": 'Kalender Promo Depo', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps1.png', "caption": 'Login', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps2.png', "caption": 'Dashboard', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps3.png', "caption": 'Master Barang', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps41.png', "caption": 'Entry Master', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps4.png', "caption": 'Tarik response BC', "order": 0},
            {"project_slug": 'tps-online', "image": 'projects/gallery/tps5.png', "caption": 'SPBB', "order": 0},
        ]
        for img_data in images_data:
            try:
                proj_obj = Project.objects.get(slug=img_data["project_slug"])
                ProjectImage.objects.update_or_create(
                    project=proj_obj,
                    image=img_data["image"],
                    defaults={
                        "caption": img_data["caption"],
                        "order": img_data["order"],
                    },
                )
            except Project.DoesNotExist:
                pass
        self.stdout.write(self.style.SUCCESS("Project images berhasil di-seed."))

        self.stdout.write(self.style.SUCCESS("Seeding company_profile SELESAI."))