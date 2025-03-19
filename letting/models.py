from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model to represent an address.

    This model stores address details including the street, city, state, zip code,
    and country ISO code.

    Attributes
    ----------
    number : PositiveIntegerField
        The street number (max 9999).
    street : CharField
        The street name (max length: 64).
    city : CharField
        The city name (max length: 64).
    state : CharField
        The two-letter state code (exact length: 2).
    zip_code : PositiveIntegerField
        The ZIP code (max 99999).
    country_iso_code : CharField
        The three-letter country ISO code (exact length: 3).

    Methods
    -------
    __str__():
        Returns a string representation of the address in the format "number street".
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a human-readable string representation of the address.

        Returns
        -------
        str
            The formatted address as "number street".
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Metadata for the Address model.

        Attributes
        ----------
        verbose_name_plural : str
            The plural name for the model in Django Admin.
        """
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    A model to represent a real estate letting.

    This model stores letting details, including a title and its associated address.

    Attributes
    ----------
    title : CharField
        The title of the letting (max length: 256).
    address : OneToOneField
        A one-to-one relationship to the `Address` model.

    Methods
    -------
    __str__():
        Returns a string representation of the letting title.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a human-readable string representation of the letting.

        Returns
        -------
        str
            The title of the letting.
        """
        return self.title
