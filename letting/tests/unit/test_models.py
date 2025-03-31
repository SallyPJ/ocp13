import pytest
from django.core.exceptions import ValidationError
from letting.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    """
    Unit tests for the Address model.

    These tests validate the string representation and field validations
    for the Address model.
    """

    def test_address_str(self, address):
        """
        Test the __str__ method of the Address model.

        Ensures that the string representation returns 'number street'.

        Parameters:
            address (Address): Fixture providing a valid Address instance.

        Returns:
            None
        """
        assert str(address) == "742 Evergreen Terrace"

    def test_address_validation_errors(self):
        """
        Test field validations for the Address model.

        Ensures that invalid field values raise a ValidationError when calling `full_clean()`.

        Returns:
            None
        """
        invalid_address = Address(
            number=10000,               # Invalid: exceeds max 9999
            street="Wall Street",
            city="New York",
            state="N",                  # Invalid: less than 2 characters
            zip_code=123456,            # Invalid: exceeds max 99999
            country_iso_code="U"        # Invalid: less than 3 characters
        )
        with pytest.raises(ValidationError):
            invalid_address.full_clean()


@pytest.mark.django_db
class TestLettingModel:
    """
    Unit tests for the Letting model.

    These tests verify the string representation and relationship with Address.
    """

    def test_letting_str(self, address):
        """
        Test the __str__ method of the Letting model.

        Ensures that the string representation returns the title of the letting.

        Parameters:
            address (Address): Fixture providing a valid Address instance.

        Returns:
            None
        """
        letting = Letting.objects.create(
            title="Downtown Loft",
            address=address
        )
        assert str(letting) == "Downtown Loft"

    def test_letting_address_relation(self, address):
        """
        Test the OneToOne relationship between Letting and Address.

        Ensures that a letting can access its linked address fields.

        Parameters:
            address (Address): Fixture providing a valid Address instance.

        Returns:
            None
        """
        letting = Letting.objects.create(
            title="Seaside Bungalow",
            address=address
        )
        assert letting.address.street == "Evergreen Terrace"
        assert letting.address.zip_code == 62704