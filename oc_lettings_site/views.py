from django.shortcuts import render


def index(request):
    """
    Render the homepage of the application.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for the homepage.
    """
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
    return render(request, 'oc_lettings_site/404.html', status=404)

def custom_500(request):
    """
    Handle 500 errors (Internal Server Error) by rendering a custom error page.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for the custom 500 error page.
    """
    return render(request, 'oc_lettings_site/500.html', status=500)

def trigger_error(request):
    """
    Trigger a custom error by raising a ValueError.

    Parameters:
        request (HttpRequest): The request object representing the incoming HTTP request.

    Raises:
        ValueError: Always raises a ValueError to simulate an internal server error.
    """
    raise ValueError("Test error for 500 page")