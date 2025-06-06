from django.shortcuts import render
from django.http import Http404
from profiles.models import Profile
import logging

logger = logging.getLogger(__name__)


def profiles_index(request):
    """
    Display a list of all user profiles.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response displaying all user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display details of a specific user profile.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.
        username (str): The username associated with the profile.

    Returns:
        HttpResponse: Rendered HTML response displaying the details of the specified user profile.
    """
    logger.info("Accessing profile for user: %s (IP: %s)",
                username, request.META.get('REMOTE_ADDR'))
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.error("Profile not found for username '%s'", username)
        raise Http404("Profile not found")
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
