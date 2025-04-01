## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### 🧭 Vue d’ensemble

Ce projet Django est conçu pour être déployé automatiquement via **Render** en utilisant **Docker** et une **pipeline CI/CD GitLab**.  
Le déploiement est déclenché **à chaque `push` sur la branche principale** grâce au fichier `.gitlab-ci.yml`.

---
### 📋 Prérequis

Avant de pouvoir déployer ce projet en production, assurez-vous de disposer des comptes et outils suivants :

### 🧑‍💻 Comptes

- ✅ Un compte **GitLab** : pour héberger le dépôt du projet et utiliser GitLab CI/CD  
  👉 https://gitlab.com

- ✅ Un compte **Render** : pour héberger l’application Django  
  👉 https://render.com

- ✅ Un compte **Docker Hub** : pour publier une image docker  
  👉 https://hub.docker.com

- ✅ Un compte **Sentry** : pour centraliser et suivre les erreurs sur l’application  
  👉 https://sentry.io

---

### ⚙️ Etapes de déploiement et Configuration requises

#### Gitlab 

##### Si nécessaire, Transférer le dépôt de GitHub vers Gitlab
 - Aller sur gitlab : https://gitlab.com/projects/new#import_project
 - Cliquer sur "Importer un projet depuis GitHub"
 - Connecter son compte GitHub si ce n’est pas encore fait 
 - Autoriser GitLab à accéder à tes dépôts GitHub 
 - Sélectionner le projet et l'importer

##### Paramétrer les variables d'environnement CI/CD
 Sur la page du dépôt gitlab :
 - Cliquer sur Settings > CI/CD > Variables
 - Appuyer sur Add Variables

| **Variable**         | **Utilisation / Où la trouver**                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------|
| `DEBUG_STATUS`       | Dans .env                                                                                          |
| `DOCKER_USERNAME`    | Dans `.gitlab-ci.yml` → utilisé pour `docker login` (push vers Docker Hub)                         |
| `DOCKER_PASSWORD`    | Dans `.gitlab-ci.yml` → utilisé avec `DOCKER_USERNAME` pour authentification Docker Hub            |
| `RENDER_DEPLOY_HOOK` | Dans `.gitlab-ci.yml` → utilisé pour déclencher le déploiement Render (`curl $RENDER_DEPLOY_HOOK`) |
| `SECRET_KEY`         | Dans `settings.py` → `SECRET_KEY = os.getenv("SECRET_KEY")`                                        |
| `SENTRY_DSN`         | Dans `settings.py` → `SENTRY_DSN = os.getenv("SENTRY_DSN", "")`                                    |

Pour que le déploiement fonctionne correctement, les éléments suivants doivent être configurés :

#### 🔐 Variables d’environnement

Les variables **doivent être définies à la fois dans Render et dans GitLab CI/CD** (`Settings > CI/CD > Variables`) :

| Variable       | Utilisation                         |
|----------------|--------------------------------------|
| `SECRET_KEY`   | Clé secrète Django                   |
| `SENTRY_DSN`   | Clé DSN pour Sentry                  |
| `DEBUG`        | ✅ Oui       | Doit être `False` en production      |
| `ALLOWED_HOSTS` | ✅ Oui       | Domaine autorisé (ex. `monapp.onrender.com`) |

---

### 🛠️ Étapes de déploiement

#### ✅ 1. Créer un service web Render

1. Aller sur [https://dashboard.render.com/](https://dashboard.render.com/)
2. Cliquer sur **New > Web Service**
3. Connecter votre dépôt GitLab
4. Configurer le service comme suit :

| Champ                  | Valeur                                            |
|------------------------|---------------------------------------------------|
| Runtime                | Python                                            |
| Build Command          | `pip install -r requirements.txt`                |
| Start Command          | `gunicorn oc_lettings_site.wsgi:application`     |
| Environment            | Python 3.10+                                      |
| Environment Variables  | Définir `SECRET_KEY`, `SENTRY_DSN`, `DEBUG=False` |

> 💡 Si vous utilisez `collectstatic`, vérifiez que `STATIC_ROOT` et `WhiteNoise` sont bien configurés.

---

#### ✅ 2. Configurer GitLab CI/CD

Dans **GitLab**, allez dans `Settings > CI/CD > Variables` et ajoutez :

- `SECRET_KEY`
- `SENTRY_DSN`
- *(Facultatif)* `DOCKER_HUB_USERNAME` et `DOCKER_HUB_TOKEN` si vous publiez une image Docker

> À chaque `push` sur la branche `main`, GitLab :
> - lance les tests,
> - construit l’image Docker,
> - déploie automatiquement sur Render.

---

#### ✅ 3. Activer Sentry

L’application est intégrée à Sentry via le code suivant dans `settings.py` :

```python
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import os

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN", ""),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)