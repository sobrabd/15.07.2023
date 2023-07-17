from django.contrib import admin
from .models import Dog, Species


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'species', 'birthday',)
    list_filter = ('species',)


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

