Deployment
==========================================

Automated Deployment
====================

Overview
--------

This project uses a **GitLab CI/CD pipeline** to automate deployment:

1. ✅ **Automatically run tests** on each push
2. 🐳 **Build a Docker image** from the project source
3. 🚀 **Publish this image to Docker Hub**
4. 🌐 **Trigger automatic deployment to Render** via webhook

Everything is triggered on each `push` to the `master` branch.

---

Prerequisites
-------------

Before deploying, make sure you have accounts on the following services:

+----------------+---------------------------------------------+-------------------------------+
| Service        | Purpose                                     | Link                          |
+================+=============================================+===============================+
| 🦊 GitLab       | Source code hosting and CI/CD              | https://gitlab.com            |
| 🐳 Docker Hub   | Hosting the built Docker image             | https://hub.docker.com        |
| 🚀 Render       | Hosting the Django web service             | https://render.com            |
| 🐛 Sentry       | Error monitoring and logging               | https://sentry.io             |
+----------------+---------------------------------------------+-------------------------------+

---

Deployment and Configuration Steps
----------------------------------

1. 📘 Sentry Configuration (error logging)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sentry is used to track and report application errors. It must be configured **before deployment**.

- Create a Sentry account (or sign in) at https://sentry.io
- Create a new project of type **Django**
- Copy your **DSN** from the project settings
- Store the DSN as an environment variable (`SENTRY_DSN`) — never hardcode it

---

2. 🐳 Docker Hub Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project uses a custom Docker image hosted on Docker Hub.
Follow these steps to create and publish your image.

**Install Docker:**

Make sure Docker is installed on your system.
🔗 https://docs.docker.com/get-started/get-docker/

**Create a repository on Docker Hub:**

- Log in to [Docker Hub](https://hub.docker.com)
- Click **"Create Repository"**
- Choose a name (e.g. `my-django-project`)
    → This will be your `DOCKER_IMAGE_NAME`
- Set visibility to **Public**
- Click **Create**

**Build your Docker image locally:**

From the root of your project (where your Dockerfile is located):

.. code-block:: bash

    docker build -t <DOCKER_USERNAME>/<DOCKER_IMAGE_NAME>:latest .

**Log in to Docker and push your image:**

.. code-block:: bash

    docker login
    docker push <DOCKER_USERNAME>/<DOCKER_IMAGE_NAME>:latest

---

3. 🚀 Render Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Go to https://dashboard.render.com
- Click **Add New > Web Service**
- Choose **"Existing Image"**
- Enter your full Docker image URL:

    .. code-block::

    docker.io/<DOCKER_USERNAME>/<DOCKER_IMAGE_NAME>:latest

- Set the following environment variables in Render:

+------------------------+-----------------------------------------------+
| Variable               | Value (customize as needed)                   |
+========================+===============================================+
| `ALLOWED_HOSTS`        | `my-app.onrender.com`                         |
| `DEBUG_STATUS`         | `False`                                       |
| `SECRET_KEY`           | Your Django secret key                        |
| `SENTRY_DSN`           | Your full Sentry DSN                          |
| `SENTRY_ENVIRONMENT`   | `production`                                  |
+------------------------+-----------------------------------------------+

---

4. 🦊 GitLab Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

**If your project isn't hosted on GitLab yet**, import it from GitHub:

- Go to https://gitlab.com/projects/new#import_project
- Click **"Import project from GitHub"**
- Log in to GitHub if needed
- Select and import your project

**Add the required CI/CD variables:**

In GitLab → **Settings > CI/CD > Variables**, add:

+------------------------+--------------------------------------------------+
| Variable               | Description                                      |
+========================+==================================================+
| `DOCKER_USERNAME`      | Your Docker Hub username                         |
| `DOCKER_PASSWORD`      | Your Docker Hub password/token                   |
| `DOCKER_IMAGE_NAME`    | Name of your Docker image                        |
| `RENDER_DEPLOY_HOOK`   | Webhook URL from Render                          |
| `SECRET_KEY`           | Your Django secret key                           |
| `SENTRY_DSN`           | Your full Sentry DSN                             |
| `DEBUG_STATUS`         | `True` (default for dev)                         |
| `ALLOWED_HOSTS`        | `127.0.0.1,localhost`                            |
| `SENTRY_ENVIRONMENT`   | `development` (for local/dev)                    |
+------------------------+--------------------------------------------------+

---

5. 🔁 Link and Push to GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your local Git repo isn't linked to GitLab yet:

.. code-block:: bash

    git remote add origin https://gitlab.com/<username>/<project-name>.git

Create a test commit:

.. code-block:: bash

    git commit --allow-empty -m "Trigger deployment"

Push to the `master` branch:

.. code-block:: bash

    git push origin master

---

✅ Once the pipeline is successful and deployment is complete, visit your app at:

.. code-block:: bash

    https://<your-render-service-name>.onrender.com
