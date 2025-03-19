from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A model to represent a user profile.

    This model extends Django's built-in User model by adding a favorite city preference.

    Attributes
    ----------
    user : OneToOneField
        A one-to-one relationship with Django's User model.
    favorite_city : CharField
        The user's favorite city (max length: 64, optional field).

    Methods
    -------
    __str__():
        Returns the username associated with the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the profile.

        Returns
        -------
        str
            The username of the associated user.
        """
        return self.user.username
