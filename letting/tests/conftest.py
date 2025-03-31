import pytest
from letting.models import Address


@pytest.fixture
def address():
    """
    Fixture that provides a valid U.S. address instance.
    """
    return Address.objects.create(
        number=742,
        street="Evergreen Terrace",
        city="Springfield",
        state="IL",
        zip_code=62704,
        country_iso_code="USA"
    )
