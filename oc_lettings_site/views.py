from django.shortcuts import render


def index(request):
    return render(request, 'oc_lettings_site/index.html')

def custom_404(request, exception):
    """Handle 404 errors (Page Not Found)"""
    return render(request, 'oc_lettings_site/404.html', status=404)

def custom_500(request):
    """Handle 500 errors (Internal Server Error)"""
    return render(request, 'oc_lettings_site/500.html', status=500)

def trigger_error(request):
    raise ValueError("Test error for 500 page")