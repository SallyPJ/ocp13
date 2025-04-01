Quickstart
==========

This guide helps you run the application locally using Docker in just a few steps.

Prerequisites
-------------

- Docker installed on your machine
- (Optional) `Invoke` installed: ``pip install invoke``

Steps to run the project locally
--------------------------------

1. Clone the project:

    .. code-block:: bash

        git clone https://gitlab.com/SallyPJ/ocp13.git
        cd ocp13

2. Build and run the Docker container:

    .. code-block:: bash

        docker pull sallypj/p13-docker:latest
        docker run -p 8000:8000 sallypj/p13-docker:latest

    The site should now be available at http://localhost:8000/

3. (Optional) Run everything with a single command using Invoke:

    .. code-block:: bash

        invoke run-local-docker

    This command pulls the latest image, runs the container, and shows the commit hash.

---