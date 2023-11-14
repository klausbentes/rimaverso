from django.urls import path
from rimaverso.views import index, buscar, selecionar_pronuncia

urlpatterns = [
    path('', index, name='index'),
    path('palavra', buscar, name='buscar'),
    path('palavra/<str:palavra>/<str:pronuncia>/', selecionar_pronuncia, name='selecionar_pronuncia'),
]
