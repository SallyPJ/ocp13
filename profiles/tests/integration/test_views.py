import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    Test if the profiles index view displays all user profiles.

    This test verifies that:
    - the page responds with 200 OK
    - the correct template is used
    - the context contains the 'profiles_list'
    - the page displays a known username

    Parameters:
        client (Client): Django test client provided by pytest-django.

    Returns:
        None
    """
    user = User.objects.create(username="homer")
    Profile.objects.create(user=user, favorite_city="Springfield")

    url = reverse('profiles:index')
    response = client.get(url)

    assert response.status_code == 200
    assert "profiles_list" in response.context
    assert "profiles/index.html" in [t.name for t in response.templates]
    assert "homer" in response.content.decode()


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Test if the profile detail view displays the correct profile information.

    This test verifies that:
    - the page responds with 200 OK
    - the correct template is used
    - the context includes the expected profile
    - the HTML includes the username and favorite city

    Parameters:
        client (Client): Django test client provided by pytest-django.

    Returns:
        None
    """
    user = User.objects.create(username="lisa")
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    url = reverse('profiles:profile', kwargs={'username': 'lisa'})
    response = client.get(url)

    assert response.status_code == 200
    assert "profile" in response.context
    assert response.context["profile"] == profile
    assert "profiles/profile.html" in [t.name for t in response.templates]
    content = response.content.decode()
    assert "lisa" in content
    assert "Paris" in content