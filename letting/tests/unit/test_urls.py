import pytest
from django.urls import reverse, resolve
from letting.views import lettings_index, letting


def test_lettings_index_url_resolves():
    """
    Test that the 'index' URL (in namespace 'letting') maps to the correct view function.
    """
    path = reverse('letting:index')  # corrected: includes namespace
    assert resolve(path).func == lettings_index


def test_letting_detail_url_resolves():
    """
    Test that the 'letting' URL (in namespace 'letting') with a parameter maps to the correct view.
    """
    path = reverse('letting:letting', kwargs={'letting_id': 1})  # corrected: includes namespace
    assert resolve(path).func == letting
