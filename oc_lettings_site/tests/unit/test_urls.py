from django.urls import reverse, resolve
from oc_lettings_site import views
from letting.views import lettings_index
from profiles.views import profiles_index

def test_root_url_resolves_to_index():
    """
    Test that the root URL ('/') resolves to the correct view function.

    This ensures that the named URL 'index' is correctly linked to the
    'index' view function in the oc_lettings_site app.
    """
    assert resolve(reverse("index")).func == views.index

def test_lettings_url_is_included():
    """
    Test that the lettings index URL resolves to the correct view function.

    This ensures that the named URL 'letting:index' correctly routes
    to the 'lettings_index' view in the letting app.
    """
    assert resolve(reverse("letting:index")).func == lettings_index

def test_profiles_url_is_included():
    """
    Test that the profiles index URL resolves to the correct view function.

    This ensures that the named URL 'profiles:index' correctly routes
    to the 'profiles_index' view in the profiles app.
    """
    assert resolve(reverse("profiles:index")).func == profiles_index