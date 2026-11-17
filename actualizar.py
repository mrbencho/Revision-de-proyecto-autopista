#!/usr/bin/env python3
"""Genera miniaturas (fotos/) y fotos.json a partir de una carpeta de originales.
Uso: python actualizar.py "D:\\Vital Impacts 2026\\raws\\Jpegs"
"""
import sys, os, json, re, unicodedata
from PIL import Image, ImageOps
src = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "fotos")
os.makedirs(out, exist_ok=True)
EXT = (".jpg", ".jpeg", ".png")
names = sorted(f for f in os.listdir(src) if f.lower().endswith(EXT))
items = []
for f in names:
    base = os.path.splitext(f)[0]
    # nombre seguro para la web: sin tildes, sin espacios, sin guion bajo inicial
    safe = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode()
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", safe).lstrip("_.") or "foto"
    dst = safe + ".jpg"
    p = os.path.join(out, dst)
    im = Image.open(os.path.join(src, f))
    im = ImageOps.exif_transpose(im).convert("RGB")
    w, h = im.size
    if not os.path.exists(p) or os.path.getmtime(p) < os.path.getmtime(os.path.join(src, f)):
        t = im.copy(); t.thumbnail((1600, 1600)); t.save(p, quality=82, optimize=True)
    items.append({"file": dst, "name": base, "w": w, "h": h})
json.dump(items, open(os.path.join(here, "fotos.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "fotos")
