from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post
from .forms import AnimalSearchForm

from Zoo.models import Area, Zone, Animal, CheckLog, DetailLog, Parttime, Zookeeper, Post
from Zoo.forms import AnimalForm


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal/animal_list.html', {'animals' : animals})


def animal_create(request):
    form = AnimalForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('animal_list')

    return render(request, 'animal/animal_form.html', {'form': form})


def animal_update(request, id):
    animal = Animal.objects.get(anm_id=id)
    form = AnimalForm(request.POST or None, instance=animal)

    if form.is_valid():
        form.save()
        return redirect('animal_list')

    return render(request, 'animal/animal_form.html', {'form': form, 'animal': animal})


def animal_delete(request, id):
    animal = Animal.objects.get(anm_id=id)

    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')

    return render(request, 'animal/animal_delete_confirm.html', {'animal': animal})

def animal_search(request):
    form = AnimalSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        animals = Animal.objects.filter(name__icontains=query)
    else:
        query = ''
        animals = Animal.objects.all()

    context = {'form': form}
    return render(request, 'animal/search.html', context)
