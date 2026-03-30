# Portfolio Django — Alex Dupont

## 🚀 Installation rapide

### 1. Créer et activer l'environnement virtuel
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Appliquer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Créer le compte admin
```bash
python manage.py createsuperuser
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

### 6. Accéder au site
- **Portfolio** → http://127.0.0.1:8000/
- **Admin** → http://127.0.0.1:8000/admin/

---

## 📝 Ajouter du contenu

Connecte-toi sur `/admin` puis :
- **Projets** → Ajouter tes projets (titre, description, technologies, liens)
- **Compétences** → Ajouter tes compétences avec niveau (0-100) et catégorie
- **Messages** → Consulter les messages reçus via le formulaire de contact

---

## 🌐 Déploiement sur Railway (gratuit)

1. Crée un compte sur https://railway.app
2. Connecte ton repo GitHub
3. Ajoute les variables d'environnement :
   - `SECRET_KEY` = une clé secrète forte
   - `DEBUG` = False
   - `ALLOWED_HOSTS` = ton-domaine.railway.app
4. Railway détecte Django automatiquement ✅

---

## 📁 Structure du projet

```
portfolio_django/
├── manage.py
├── requirements.txt
├── portfolio_django/
│   ├── settings.py
│   └── urls.py
└── portfolio/
    ├── models.py       ← Projet, Compétence, Message
    ├── views.py        ← Logique des pages
    ├── forms.py        ← Formulaire de contact
    ├── admin.py        ← Configuration de l'admin
    └── templates/
        └── portfolio/
            └── home.html
```
