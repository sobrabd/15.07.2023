from django.shortcuts import render
from .models import Species, Dog


def home(request):
    context = {
        "object_list": Species.objects.all()
    }
    return render(request, 'dogs/index.html', context)


def species(request):
    context = {
        "object_list": Species.objects.all()
    }
    return render(request, 'dogs/species.html', context)


def single_specie(request, pk):
    context = context = {
        'object_list': Dog.objects.filter(species=pk)
    }
    return render(request, 'dogs/single_species.html', context)