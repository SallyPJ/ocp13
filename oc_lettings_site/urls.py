from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('letting.urls', namespace="letting")),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('admin/', admin.site.urls),
    path('trigger-error/', views.trigger_error),

]

handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'