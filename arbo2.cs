altaris/
│
├── altaris/                  # Dossier du projet principal
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Fichier de configuration principal
│   ├── urls.py               # Routeur principal des URLs
│   ├── wsgi.py
│   └── static/               # Fichiers statiques globaux (CSS, JS, etc.)
│
├── geographie/               # Application pour la gestion géographique
│   ├── migrations/           # Fichiers de migration
│   ├── templates/            # Templates HTML liés à la géographie
│   │   └── geographie/       # Dossier de templates spécifiques à cette app
│   ├── __init__.py
│   ├── admin.py              # Gestion des modèles via l'admin Django
│   ├── apps.py               # Configuration de l'application
│   ├── models.py             # Modèles : Province, Diocese, Zone, Paroisse
│   ├── urls.py               # Routes spécifiques à cette application
│   ├── views.py              # Logique des vues
│   └── tests.py              # Tests unitaires pour cette application
│
├── bureau/                   # Application pour la gestion des bureaux
│   ├── migrations/
│   ├── templates/
│   │   └── bureau/           # Templates spécifiques aux bureaux
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modèles : Bureau, PosteBureau, ServantPosteBureau
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── servants/                 # Application pour la gestion des servants d'autel
│   ├── migrations/
│   ├── templates/
│   │   └── servants/         # Templates pour l'affichage des servants
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modèle : Servant
│   ├── urls.py
│   ├── views.py
│   ├── forms.py              # Formulaires pour la gestion des servants
│   └── tests.py
│
├── utilisateurs/             # Application pour la gestion des utilisateurs
│   ├── migrations/
│   ├── templates/
│   │   └── utilisateurs/     # Templates pour l'inscription/connexion des utilisateurs
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modèle : Utilisateur
│   ├── urls.py
│   ├── views.py
│   ├── forms.py              # Formulaires pour les utilisateurs
│   ├── managers.py           # Custom User Manager (si nécessaire)
│   └── tests.py
│
├── common/                   # Application facultative pour les utilitaires
│   ├── migrations/
│   ├── templates/
│   │   └── common/           # Templates pour des fonctionnalités communes
│   ├── __init__.py
│   ├── apps.py
│   ├── utils.py              # Fonctions utilitaires (ex. : génération de QR codes)
│   ├── services.py           # Services partagés (ex. : envoi d'emails, notifications)
│   ├── urls.py
│   └── tests.py
│
├── media/                    # Fichiers média uploadés (photos des servants, etc.)
│   └── servants/
│       └── photos/           # Répertoire pour les photos des servants
│
├── static/                   # Fichiers statiques partagés (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/                # Dossier général pour les templates partagés
│   ├── base.html             # Template de base pour le projet
│   ├── includes/             # Fragments de templates réutilisables
│   └── layout/               # Templates pour les layouts globaux
│
├── manage.py                 # Commande de gestion Django
└── requirements.txt          # Dépendances du projet (bibliothèques Python)
