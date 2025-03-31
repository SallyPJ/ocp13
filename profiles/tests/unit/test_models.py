import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """
    Test the __str__ method of the Profile model.

    Ensures that the string representation returns the username of the associated user.

    Returns:
        None
    """
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="New York")
    assert str(profile) == "testuser"