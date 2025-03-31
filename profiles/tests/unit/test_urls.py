from django.urls import reverse, resolve
from profiles import views


def test_profiles_index_url_resolves():
    """
    Test that the 'profiles:index' URL resolves to the profiles_index view.

    Returns:
        None
    """
    path = reverse('profiles:index')
    assert resolve(path).func == views.profiles_index


def test_profile_detail_url_resolves():
    """
    Test that the 'profiles:profile' URL resolves to the profile view with a username.

    Returns:
        None
    """
    path = reverse('profiles:profile', kwargs={'username': 'testuser'})
    assert resolve(path).func == views.profile
