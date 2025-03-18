from django.urls import path
from . import views

app_name = "letting"

urlpatterns = [
    path('', views.lettings_index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
