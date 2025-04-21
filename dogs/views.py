from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from dogs.models import Breed, Dog
from dogs.forms import DogForms


def index_view(request):
    context = {
        'object_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }

    return render(request, 'dogs/index.html', context=context)


def breeds_list_view(request):
    context = {
        'object_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context=context)


def breed_dogs_list_view(request, pk: int):
    breed_object = Breed.objects.get(pk=pk)
    context = {
        'objects_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - {breed_object.name}',
        'breed_pk': breed_object.pk
    }
    return render(request, 'dogs/dogs.html', context=context)


def dogs_list_view(request):
    context = {
        'object_list': Dog.objects.all(),
        'title': f'Все наши собаки',
    }
    return render(request, 'dogs/dogs.html', context=context)


# Create Read Update Delete (CRUD)
@login_required(login_url='users:user_login')
def dog_create_view(request):
    if request.method == 'POST':
        form = DogForms(request.POST, request.FILES)
        if form.is_valid():
            dog_object = form.save()
            dog_object.owner = request.user
            dog_object.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'title': 'Добавить собаку',
        'form': DogForms
    }
    return render(request, 'dogs/create_update.html', context=context)
    # return render(request, 'dogs/create.html', {'form': DogForms})   пример без context


@login_required(login_url='users:user_login')
def dog_detail_view(request, pk):
    dog_object = Dog.objects.get(pk=pk)
    context = {'object': dog_object,
               'title': dog_object
               }
    return render(request, 'dogs/detail.html', context=context)


@login_required(login_url='users:user_login')
def dog_update_view(request, pk):
    dog_object = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        form = DogForms(request.POST, request.FILES, instance=dog_object)
        if form.is_valid():
            dog_object = form.save()
            dog_object.save()
            return HttpResponseRedirect(reverse('dogs:dog_detail', args={pk: pk}))
    context = {
        'object': dog_object,
        'title': 'Изменить собаку',
        'form': DogForms(instance=dog_object)
    }
    return render(request, 'dogs/create_update.html', context=context)


@login_required(login_url='users:user_login')
def dog_delete_view(request, pk):
    dog_object = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        dog_object.delete()
    context = {
        'object': dog_object,
        'title': 'Удалить собаку',
    }
    return render(request, 'dogs/delete.html', context=context)
