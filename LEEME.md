# Tablero de fotos Vital Impacts

Abrir en local: en esta carpeta ejecutar `python -m http.server 8000` y entrar a http://localhost:8000
(abrir index.html con doble clic no funciona, el navegador bloquea fotos.json).

## Actualizar con fotos nuevas
1. Requiere Python y Pillow: `pip install pillow`
2. `python actualizar.py "D:\Vital Impacts 2026\raws\Jpegs"`
   (crea miniaturas en fotos/ y regenera fotos.json; las fotos nuevas aparecen debajo de las existentes)
3. `git add . && git commit -m "fotos nuevas" && git push`

## Orden compartido
El orden que armes se guarda en tu navegador. Para que otros lo vean igual:
botón "Exportar layout" -> guardar el archivo como layout.json en esta carpeta -> subir al repo.
