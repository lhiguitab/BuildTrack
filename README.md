# BuildTrack API

API de seguimiento de proyectos de construcción para BuildRight Contractors.

## Ejecución local

Instala las dependencias una vez:

```powershell
python -m pip install -r requirements.txt
```

Inicia la API desde la raíz del repositorio con un solo comando:

```powershell
python -m uvicorn main:app --app-dir src --reload
```

La documentación interactiva queda disponible en `http://127.0.0.1:8000/docs`.

## Pruebas

```powershell
python -m unittest discover -s tests -v
```
