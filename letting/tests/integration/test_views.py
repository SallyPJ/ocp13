import pytest
from django.urls import reverse
from letting.models import Letting


@pytest.mark.django_db
def test_lettings_index_view(client, address):
    """
    Test if the lettings index view displays the list of lettings correctly.

    This test verifies that:
    - the index view returns an HTTP 200 response
    - the context contains the 'lettings_list' variable
    - the correct template is used
    - the rendered HTML includes the letting title

    Parameters:
        client (Client): Django test client provided by pytest-django.
        address (Address): Fixture providing a valid Address instance.

    Returns:
        None
    """
    Letting.objects.create(title="Cozy Cottage", address=address)
    url = reverse('letting:index')
    response = client.get(url)

    # Check status
    assert response.status_code == 200

    # Check context
    assert "lettings_list" in response.context

    # Check template
    assert "letting/index.html" in [t.name for t in response.templates]

    # Check content
    html = response.content.decode()
    assert "Cozy Cottage" in html


@pytest.mark.django_db
def test_letting_detail_view(client, address):
    """
    Test if the letting detail view displays correct information.

    This test checks the detail view of a Letting object. It ensures that:
    - the page responds with HTTP 200
    - the correct template is used
    - the context contains the expected 'title' and 'address'
    - the rendered HTML includes all address components

    Parameters:
        client (Client): Django test client provided by pytest-django.
        address (Address): Fixture providing a valid Address instance.

    Returns:
        None
    """
    letting = Letting.objects.create(title="Seaside Villa", address=address)
    url = reverse('letting:letting', kwargs={"letting_id": letting.id})
    response = client.get(url)

    # Check status
    assert response.status_code == 200

    # Check context variables
    assert "title" in response.context
    assert response.context["title"] == "Seaside Villa"
    assert "address" in response.context
    assert response.context["address"] == address

    # Check template used
    assert "letting/letting.html" in [t.name for t in response.templates]

    # Check content
    content = response.content.decode()
    assert "Seaside Villa" in content
    assert str(address.number) in content
    assert address.street in content
    assert address.city in content
    assert address.state in content
    assert str(address.zip_code) in content
    assert address.country_iso_code in content
