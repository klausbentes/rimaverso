from django.urls import path
from rimaverso.views import index, buscar

urlpatterns = [
    path('', index, name='index'),
    path('buscar', buscar, name='buscar'),
]