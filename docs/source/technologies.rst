Technologies and Languages Used
===============================

Languages
---------

- **Python 3** – Main programming language.
- **HTML / CSS** – Used for templates and styling.
- **reStructuredText (reST)** – Used to write the documentation (Sphinx-compatible).

Frameworks and Core Libraries
-----------------------------

- **Django 3.0** – Web framework used to build the application.
- **Gunicorn** – WSGI server to run the app in production.
- **Whitenoise** – Serves static files in production without external web server.

Deployment and Hosting
-----------------------

- **Docker** – Containerization of the application for reproducible environments.
- **Docker Hub** – Hosts the Docker image built by the CI pipeline.
- **Render** – Pulls and runs the Docker image to deploy the Django app.

Environment and Configuration
-----------------------------

- **python-dotenv** – Manages environment variables via `.env` files.
- **Invoke** – Used to define and run command-line tasks (via `tasks.py`).

DevOps and CI/CD
----------------

- **Git** – Version control system.
- **GitLab CI/CD** – Automates testing, image building and deployment.

Testing and Coverage
--------------------

- **pytest** – Test runner for unit and integration tests.
- **pytest-django** – Django integration for pytest.
- **pytest-cov** – Coverage plugin for pytest.

Linting and Code Quality
------------------------

- **flake8** – Linting tool for Python code style and quality.

Monitoring and Logging
----------------------

- **sentry-sdk** – Captures and logs application errors to Sentry.

Documentation
----------------------

- **Sphinx** – Documentation generator.
- **sphinx-rtd-theme** – Theme used for Read the Docs integration.
- **sphinx-autodoc-typehints** – Automatically documents type hints in functions/classes.
