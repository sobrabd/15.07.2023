from django.urls import path
from .apps import DogsConfig

from . import views

app_name = DogsConfig.name
urlpatterns = [
    path("", views.home, name="home"),
    path("species/", views.species, name="species"),
    path("species/<int:pk>", views.single_specie, name="species_list"),

]
