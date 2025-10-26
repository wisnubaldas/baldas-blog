---
date: 2025-10-27
source: https://chatgpt.com/g/g-p-68e160573f788191a5082f39ded84158-backend-fastapi/c/68f76058-de34-8323-b433-361e88c94186
author: Baldas
title: "backend fastapi - Isi TUJUAN dengan CGK"
tags:
  - mkdocs
  - tutorial
summary: "backend fastapi - Isi TUJUAN dengan CGK"
---

✅ Betul — error itu muncul karena field `TUJUAN` di Pydantic **tidak menerima `None`**, tetapi nilai dari database (`row_dict`) ternyata `None`.  
Pesan error:

```pgsql
Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
```

artinya Pydantic mengira `TUJUAN` wajib berupa string, tapi dikasih `None`.

<!-- more -->

### 💡 Cara memperbaiki

Gunakan anotasi tipe **opsional (`| None`)** _dan_ beri **default value** supaya aman saat `None` dikirim.

#### ✅ Contoh benar (Pydantic v2)

```python
from pydantic import BaseModel, Field

class AP2SendInv(BaseModel):
    USR: str
    PSW: str
    TUJUAN: str | None = Field(default="CGK", description="Kode tujuan default CGK")

```

> Artinya:
>
> - Jika `TUJUAN` tidak dikirim, maka otomatis `"CGK"`
> - Jika `TUJUAN=None`, Pydantic tetap valid (karena tipe `| None`)
> - Jika kamu ingin **selalu ubah `None` → 'CGK'**, bisa pakai `model_post_init`

---

### ⚙️ Jika kamu ingin memastikan tidak ada nilai `None` yang lolos:

Gunakan `model_post_init` (fitur Pydantic v2) untuk set default manual:

```python
from pydantic import BaseModel, Field

class AP2SendInv(BaseModel):
    USR: str
    PSW: str
    TUJUAN: str | None = Field(default=None)

    def model_post_init(self, __context):
        if self.TUJUAN is None:
            self.TUJUAN = "CGK"

```

Dengan cara ini, meskipun `row_dict["TUJUAN"] = None`, instance tetap punya `TUJUAN="CGK"` setelah validasi.

---

### 🔍 Atau solusi paling aman di `send_invoice()` sebelum membuat schema:

```python
row_dict["TUJUAN"] = row_dict.get("TUJUAN") or "CGK"
schema = AP2SendInv(USR=ENV.AP2_USER, PSW=ENV.AP2_PASSWORD, **row_dict)

```

---

### 📘 Kesimpulan

| Tujuan                               | Solusi                                                     |
| ------------------------------------ | ---------------------------------------------------------- |
| Mengizinkan None                     | \`TUJUAN: str                                              |
| Mengganti None jadi default otomatis | Gunakan `model_post_init`                                  |
| Perbaiki sebelum instansiasi         | Set `row_dict["TUJUAN"] = row_dict.get("TUJUAN") or "CGK"` |

---

Apakah kamu ingin saya bantu refactor seluruh schema `AP2SendInv` supaya semua field yang rawan `None` otomatis punya default seperti ini (biar tidak error saat dijalankan di scheduler)?
