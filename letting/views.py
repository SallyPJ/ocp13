from django.shortcuts import render
from django.http import Http404
from .models import Letting
import logging

logger = logging.getLogger(__name__)


def lettings_index(request):
    """
    Display a list of all available lettings.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response displaying all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/index.html', context)


def letting(request, letting_id):
    """
    Display details of a specific letting.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.
        letting_id (int): The unique identifier of the letting.

    Returns:
        HttpResponse: Rendered HTML response displaying the details of the specified letting.
    """
    logger.info("Letting page accessed(IP: %s)", letting_id, request.META.get('REMOTE_ADDR'))
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.error("Letting not found", letting_id)
        raise Http404("Letting not found")
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)
