# antifeu (projet)

Petit projet Django pour gérer des incidents d'incendie.

Prérequis:
- Python 3.11+ (ou compatible avec Django 5.1.6)

Installation (Windows `cmd.exe`):

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd antifeu
python manage.py migrate
python manage.py createsuperuser  # optionnel
python manage.py runserver
```

Points utiles:
- API incidents: `/api/incidents/`
- Docs OpenAPI (Swagger): `/api/docs/`
- Media uploads: `MEDIA_ROOT` défini sur le dossier `media/` à la racine du projet
