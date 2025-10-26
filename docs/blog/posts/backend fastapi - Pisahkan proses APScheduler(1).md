---
date: 2025-10-27
source: https://chatgpt.com/g/g-p-68e160573f788191a5082f39ded84158-backend-fastapi/c/68f76058-de34-8323-b433-361e88c94186
author: Baldas
title: "Pisahkan proses APScheduler"
tags:
  - mkdocs
  - tutorial
summary: Pisahkan proses APScheduler
---

# backend fastapi - Pisahkan proses APScheduler

> ## Excerpt
>
> A conversational AI system that listens, learns, and challenges

---

Pertanyaan sangat bagus ⚙️  
Kamu ingin **APScheduler** tetap jalan _sendiri_ (sebagai service terpisah) tanpa harus menjalankan `main.py` FastAPI — ini sangat umum dilakukan untuk sistem produksi agar job scheduler tidak mati saat API direstart.

<!-- more -->

---

## 🔍 Tujuan

Pisahkan proses APScheduler agar:

- Tidak ikut di dalam proses FastAPI (`main.py`)
- Bisa dijalankan sendiri (misal lewat `supervisor`, `systemd`, atau `docker`)
- Tapi tetap menggunakan modul, service, dan database yang sama dengan aplikasi FastAPI

---

## ✅ 1. Struktur Folder Disarankan

Misal struktur proyek kamu:

```bash
app/
├── api/
│   └── user_route.py
├── core/
│   └── config.py
├── db/
│   └── mysql.py
├── jobs/
│   ├── scheduler.py          # <-- jadwal & fungsi scheduler
│   ├── tasks/
│   │   ├── run_breakdown.py
│   │   └── run_incoming.py
├── main.py                   # FastAPI utama
└── services/
    └── ...

```

---

## ✅ 2. Buat file `app/jobs/scheduler.py`

Ini file **standalone APScheduler runner**, tidak tergantung FastAPI:

```python
# app/jobs/scheduler.py
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
import logging

from app.db.mysql import SessionDB1W  # contoh pakai koneksi DB yang sama
from app.services.inv_ap2_service import run_breakdown, run_incoming

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

scheduler = AsyncIOScheduler()

def init_scheduler():
    scheduler.add_job(run_breakdown, "interval", seconds=10, id="breakdown_job")
    scheduler.add_job(run_incoming, "interval", seconds=11, id="incoming_job")
    logging.info("✅ Jobs registered")

async def start_scheduler():
    init_scheduler()
    scheduler.start()
    logging.info("✅ APScheduler started")

    # biar tidak keluar
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown(wait=False)
        logging.info("🛑 APScheduler stopped")

if __name__ == "__main__":
    asyncio.run(start_scheduler())

```

Jalankan:

```bash
poetry run python -m app.jobs.scheduler

```

Atau jika tanpa poetry:

```bash
python -m app.jobs.scheduler

```

---

## ✅ 3. Jalankan Terpisah dari FastAPI

### Opsi A — via Supervisor

Buat file `/etc/supervisor/conf.d/apscheduler.conf`:

```ini
[program:apscheduler]
directory=/home/wisnu/mau-app/materialize-fastapi
command=/home/wisnu/mau-app/materialize-fastapi/.venv/bin/python -m app.jobs.scheduler
autostart=true
autorestart=true
stderr_logfile=/var/log/apscheduler_error.log
stdout_logfile=/var/log/apscheduler_output.log
user=wisnu

```

Restart:

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start apscheduler

```

---

### Opsi B — via Systemd

Buat `/etc/systemd/system/apscheduler.service`:

```ini
[Unit]
Description=APScheduler for FastAPI
After=network.target

[Service]
WorkingDirectory=/home/wisnu/mau-app/materialize-fastapi
ExecStart=/home/wisnu/mau-app/materialize-fastapi/.venv/bin/python -m app.jobs.scheduler
Restart=always
User=wisnu

[Install]
WantedBy=multi-user.target

```

Lalu:

```bash
sudo systemctl daemon-reload
sudo systemctl enable apscheduler
sudo systemctl start apscheduler
sudo systemctl status apscheduler

```

---

## ✅ 4. (Opsional) Berbagi Log dan Config

Agar `scheduler.py` tetap sinkron dengan konfigurasi FastAPI:

- Gunakan `from app.core.config import ENV`
- Gunakan logger terpusat (`logging_utils.py`)
- Gunakan database session (`SessionDB1W`, `SessionDB2R`, dsb.)

---

## ✅ 5. (Opsional) Monitoring & Redis JobStore

Jika kamu ingin job tetap bertahan meskipun service restart:

```python
from apscheduler.jobstores.redis import RedisJobStore

jobstores = {
    "default": RedisJobStore(host="localhost", port=6379, db=0)
}

scheduler = AsyncIOScheduler(jobstores=jobstores)

```

---

## 🚀 Hasil Akhir

- `main.py` → hanya menjalankan FastAPI
- `scheduler.py` → jalan mandiri, bisa diatur, dipantau, dan restart otomatis
- Aman untuk production (isolasi job, error log terpisah, dll.)

---

Kalau mau, saya bisa bantu buatkan **versi siap-pakai untuk Supervisor dan Systemd**, lengkap dengan logging dan contoh file `.env` agar APScheduler ikut baca variabel environment aplikasi utama.  
Apakah kamu ingin saya buatkan versi itu juga?
