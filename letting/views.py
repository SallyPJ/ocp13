from django.shortcuts import render
from .models import Letting


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
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)
