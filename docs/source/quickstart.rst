Quickstart
===========

You can run the project in two ways:

1. Locally (recommended for development)
2. From a Docker image

Shared Configuration (Local & Docker)
----------------------------------------

Before running the project in any environment (local or Docker), make sure to configure the following environment variables.

1. **Generate a SECRET_KEY:**

    Generate a random secret key using the following command and keep it:

    .. code-block:: bash

        python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

2. **Get a sentry DSN**
    - Go to https://sentry.io
    - Log in or create an account
    - Click on Projects → Create Project
    - Select Django as the platform
    - Name your project
    - Keep the code snippet with a DSN

3. **Set up environment variables:**

    Create a `.env` file at the project root with the following content:

    .. code-block:: bash

        DEBUG_STATUS=True
        SECRET_KEY=your_secret_key
        SENTRY_DSN=your_sentry_dsn
        ALLOWED_HOSTS=localhost,127.0.0.1
        SENTRY_ENVIRONMENT=development

Local setup
-------------

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~

- the project is installed (See "Installation")
- Python ≥ 3.8 is available
- Virtual environment is activated


Steps to run the project locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. **Collect static files:**

    .. code-block:: bash

        python manage.py collectstatic --noinput

5. **Run the server locally:**

    Now you can start the server by running:

    .. code-block:: bash

        python manage.py runserver

Then, open your browser and go to  http://localhost:8000


Docker setup
--------------

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~

- Docker installed and running on your machine

Steps to run the project
~~~~~~~~~~~~~~~~~~~~~~~~~~

Build and run locally the Docker container:

    .. code-block:: bash

        docker build -t your_project_name:tag .
        docker run --env-file .env -p 8000:8000 your_project_name:tag

The site should now be available at http://localhost:8000/

