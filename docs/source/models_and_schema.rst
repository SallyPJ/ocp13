Models and Database Schema
==========================================

This section provides an overview of the Django models used in the project, along with a visual representation of the database schema.

Models
--------------------------------
Below are the core models of the application, with their fields and methods auto-documented:

**Lettings App:**

.. autoclass:: letting.models.Address
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects
   :no-index:

.. autoclass:: letting.models.Letting
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects
   :no-index:

**Profiles App:**

.. autoclass:: profiles.models.Profile
   :members:
   :exclude-members: DoesNotExist, MultipleObjectsReturned, objects
   :no-index:

Database schema diagram
--------------------------------
The following diagram illustrates the relationships between the models:

.. image:: _static/db_schema.png
   :alt: Database Schema Diagram
   :align: center
   :width: 80%