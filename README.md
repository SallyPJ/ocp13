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
- `git clone https://github.com/SallyPJ/ocp13.git`

#### Créer l'environnement virtuel

- `cd /path/to/ocp13`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/ocp13`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/ocp13`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/ocp13`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/ocp13`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## 🚀 Déploiement automatique

### 🧭 Vue d’ensemble

Pour le déploiement, on utilise une **pipeline GitLab CI/CD** pour :

1. ✅ **Exécuter automatiquement les tests** de l’application 
2. 🐳 **Construire une image Docker** à partir du code du projet
3. 🚀 **Publier cette image sur Docker Hub**
4. 🌐 **Déployer automatiquement l'application sur Render** via un webhook

Tout cela est déclenché à chaque `push` sur la branche `master`.


### 📋 Prérequis

Avant le déploiement, vérifiez que vous disposez des comptes suivants :

| Compte / Service | Usage | Lien |
|------------------|-------|------|
| 🦊 **GitLab** | Gestion du code source et CI/CD | [gitlab.com](https://gitlab.com) |
| 🐳 **Docker Hub** | Stockage de l'image Docker | [hub.docker.com](https://hub.docker.com) |
| 🚀 **Render** | Hébergement du service web Django | [render.com](https://render.com) |
| 🐛 **Sentry** | Monitoring des erreurs | [sentry.io](https://sentry.io) |



### ⚙️ Étapes de déploiement et configuration

#### 1. 📘 Configuration Sentry (journalisation des erreurs)

Sentry est utilisé pour suivre les erreurs et exceptions dans l’application. Il doit être configuré **avant** le déploiement.

- Créez un compte (ou connectez-vous) sur [sentry.io](https://sentry.io)
- Créez un nouveau projet Sentry de type **Django**
- Récupérez le **DSN** dans la page de configuration du projet
- Conservez-le **en tant que variable d’environnement** (`SENTRY_DSN`).

#### 2. 🐳 Configuration Docker Hub

Ce projet utilise une image Docker personnalisée hébergée sur Docker Hub.  
Voici les étapes pour créer cette image et la rendre disponible pour Render ou toute autre plateforme de déploiement.


#####  Installer Docker

Avant tout, assurez-vous que Docker est installé sur votre machine.  
🔗 [Télécharger Docker](https://docs.docker.com/get-started/get-docker/)


#####  Créer un dépôt sur Docker Hub

- Connectez-vous sur [Docker Hub](https://hub.docker.com)
- Cliquez sur **"Create Repository"**
- Donnez un nom à votre dépôt, par exemple : `mon-projet-django`  
  👉 Ce nom sera utilisé dans la variable `DOCKER_IMAGE_NAME`
- Définissez la visibilité sur **Public** 
- Cliquez sur **Create**



##### Construire l’image Docker localement

Depuis la **racine de votre projet** (là où se trouve le fichier `Dockerfile`), exécutez la commande suivante :

```bash
docker build -t <DOCKER_USERNAME>/<DOCKER_IMAGE_NAME>:latest .
```
##### Se connecter à docker et pusher l'image 
- Connectez vous à docker :
```bash
 docker login
 ```
- Publiez l'image sur dockerhub :
```bash
  docker push <DOCKER_USERNAME>/<DOCKER_IMAGE_NAME>:latest
```

#### 3. 🚀 Configuration Render

- Connectez-vous sur [dashboard.render.com](https://dashboard.render.com).
- Cliquez sur **Add New > Web Service**.
- Sélectionnez **Existing Image**.
- Renseignez l'URL complète de votre image Docker :

  ```
  docker.io/{DOCKER_USERNAME}/{DOCKER_IMAGE_NAME}:latest
  ```

- Définissez les variables d’environnement suivantes dans Render :

| Variable            | Valeur (à personnaliser)                                 |
|---------------------|-----------------------------------------------------------|
| `ALLOWED_HOSTS`     | `my-app.onrender.com` (remplacer par votre URL Render)   |
| `DEBUG_STATUS`      | `False`                                                   |
| `SECRET_KEY`        | Votre clé secrète Django                                 |
| `SENTRY_DSN`        | URL DSN Sentry                                           |
| `SENTRY_ENVIRONMENT`| `production`                                             |


#### 4. 🦊 Configuration GitLab

Si le projet n'est pas hébergé sur Gitlab, importez le dépôt depuis GitHub :

- Connectez-vous sur [GitLab](https://gitlab.com/projects/new#import_project).
- Cliquez sur **Importer un projet depuis GitHub**.
- Connectez votre compte GitHub si nécessaire.
- Importez le projet.

##### 🔐 Variables d’environnement CI/CD

Dans GitLab, allez sur : **Settings > CI/CD > Variables**, puis ajoutez ces variables :

| Variable            | Valeur / Description                                  |
|---------------------|--------------------------------------------------------|
| `DOCKER_USERNAME`   | Votre identifiant Docker Hub                          |
| `DOCKER_PASSWORD`   | Votre mot de passe Docker Hub                         |
| `DOCKER_IMAGE_NAME` | Le nom de votre image Docker Hub                      |
| `RENDER_DEPLOY_HOOK`| Webhook Render (à récupérer depuis Render)            |
| `SECRET_KEY`        | Clé secrète Django                                    | 
| `ALLOWED_HOSTS`     | `127.0.0.1,localhost`              |

##### Associer le dépôt local au dépôt distant Gitlab et pusher pour activer la pipeline
- Associer si nécessaire le repo git local au repo gitlab distant  
```bash
  git remote add origin https://gitlab.com/<username>/<nom-du-projet>.git
```
- Effectuer un commit de test
```bash
  git commit --allow-empty -m "Test"
```
- Pusher le commit sur la branche master du repo Gitlab
```bash
  git push gitlab master 
```
Une fois le déploiement en succès sur render, ouvrir l'application :
```bash
  https://<nom-de-ton-service>.onrender.com
```

## 📚 Documentation
La documentation en anglais complète du projet se trouve ici :
https://ocp13-sallypj.readthedocs.io/en/latest/




