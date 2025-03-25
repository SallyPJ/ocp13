from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the homepage of the application.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for the homepage.
    """
    logger.info("Page d'accueil accédée depuis l'IP : %s", request.META.get('REMOTE_ADDR'))

    return render(request, 'oc_lettings_site/index.html')

def custom_404(request, exception):
    """
    Handle 404 errors (Page Not Found) by rendering a custom error page.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: Rendered HTML response for the custom 404 error page.
    """
    logger.warning("404 - Page non trouvée : %s", request.path)
    return render(request, 'oc_lettings_site/404.html', status=404)

def custom_500(request):
    """
    Handle 500 errors (Internal Server Error) by rendering a custom error page.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for the custom 500 error page.
    """
    logger.critical("500 - Erreur interne survenue lors du traitement de %s", request.path)
    return render(request, 'oc_lettings_site/500.html', status=500)

def test_error(request):
    logger.error("Déclenchement volontaire d'une erreur pour test Sentry")
    division_by_zero = 1 / 0