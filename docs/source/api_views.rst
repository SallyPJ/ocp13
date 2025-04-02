Application Programming Interface
=========================================

The Django project is organized into **three separate apps**, each with its own purpose and responsibilities:

- **oc_lettings_site**
  The main project app. It contains the site's core configuration, the home page view, custom error handlers, and the global layout.

- **letting**
  Manages the lettings section. Each letting is associated with a dedicated address model.
  Provides views for listing and displaying lettings.

- **profiles**
  Manages user profile data. Each profile is linked to a Django user and includes additional information such as a favorite city.
  Provides views for listing profiles and displaying details.

Available Views
---------------

**Lettings app**

- `lettings_index(request)`
  Displays a list of all lettings.

- `letting_detail(request, letting_id)`
  Displays detailed information for a single letting, based on its ID.

**Profiles app**

- `profiles_index(request)`
  Displays a list of all user profiles.

- `profile_detail(request, username)`
  Displays detailed information about a profile based on the username.

**Main site app**

- `index(request)`
  Displays the home page.

- `custom_404(request, exception)`
  Custom error handler for 404 errors.

- `custom_500(request)`
  Custom error handler for 500 errors.

- `test_error(request)`
  Triggers a deliberate error (used for Sentry testing).

Routes and Usage
----------------

These views are accessible through their corresponding routes:

- ``/`` → Homepage
- ``/lettings/`` → Lettings index
- ``/lettings/<id>/`` → Letting detail
- ``/profiles/`` → Profiles index
- ``/profiles/<username>/`` → Profile detail
- ``/admin/`` → Admin interface (requires superuser login)
- ``/debug-sentry/`` → Manually trigger a 500 error for Sentry testing

