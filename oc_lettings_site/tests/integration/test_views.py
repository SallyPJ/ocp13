import pytest
from django.urls import reverse


def test_index_view(client):
    """
    Test if the index page loads correctly.

    Parameters:
            client (Client): Django test client.

    Returns:
            None
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "Welcome" in response.content.decode()

def test_custom_404(client):
    """
    Test if the custom 404 error page is displayed correctly.

    Parameters:
        client (Client): Django test client.

    Returns:
        None
    """
    response = client.get("/non-existent-page/")
    assert response.status_code == 404
    assert "Page Not Found" in response.content.decode()




