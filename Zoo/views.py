from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import AnimalSearchForm
from django.shortcuts import render, get_object_or_404
from Zoo.models import Area, Zone, Animal, CheckLog, DetailLog, Parttime, Zookeeper, Post
from Zoo.forms import AnimalForm



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

from django.shortcuts import render, get_object_or_404
from .models import Animal,Zone

def zone(request):
    return render(request, 'zone.html')

def detail(request):
    return render(request, 'animal_detail.html')

def animal_list(request):
    animals = Animal.objects.all()
    context = {'animals': animals}
    return render(request, 'index.html', context)

from Zoo.forms import CheckLogForm


##여기 아직 미완성
def checklog_create(request):
    if request.method == 'POST':
        form = CheckLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = CheckLogForm()

    return render(request, 'checklog/checklog_create.html', {'form': form})


def search(request):
    blogs = Blog.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'search.html')
