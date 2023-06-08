from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post
from .forms import AnimalSearchForm
from django.shortcuts import render, get_object_or_404
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

def zkp_main(request):
    # 메인 페이지를 나타내는 데이터 로직
    return render(request, 'zkpmain.html')

def animal_detail(request):
    monkey_animals = Animal.objects.filter(anm_spcs="Monkey")
    return render(request, 'zoogle/animal_detail.html', {'monkey_animals': monkey_animals})

def animal_zone(request, anm_spcs):
    animal = get_object_or_404(Animal, anm_spcs=anm_spcs)
    # 해당 anm_spcs에 대한 데이터 로직
    return render(request, 'zoogle/zone.html', {'animal': animal})