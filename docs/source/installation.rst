Installation
==========================================

To install and set up the OCP13 project locally, follow these steps:

1. **Clone the repository:**

    .. code-block:: bash

        git clone https://gitlab.com/SallyPJ/ocp13
        cd ocp13

2. **Create and activate a virtual environment :**

    .. code-block:: bash

        python3 -m venv venv # On Windows : python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install the dependencies:**

    .. code-block:: bash

        pip install -r requirements.txt

4. **Generate a SECRET_KEY:**

    Generate a random secret key using the following command and keep it:

    .. code-block:: bash
        python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

5. **Get a sentry DSN**
    - Go to https://sentry.io
    - Log in or create an account
    - Click on Projects → Create Project
    - Select Django as the platform
    - Name your project
    - Keep the code snippet with a DSN

5. **Set up environment variables:**

    Create a `.env` file at the project root with the following content:

    .. code-block:: dotenv

        DEBUG_STATUS=True
        SECRET_KEY=your_secret_key
        SENTRY_DSN=your_sentry_dsn
        ALLOWED_HOSTS=localhost,127.0.0.1
        SENTRY_ENVIRONMENT=development

6. **Collect static files:**

    .. code-block:: bash

        python manage.py collectstatic --noinput

7. **Run the server locally:**

    Now you can start the server by running:

    .. code-block:: bash
        python manage.py runserver

    Then, open your browser and go to  http://localhost:8000