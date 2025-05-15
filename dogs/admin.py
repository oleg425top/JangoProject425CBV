from django.contrib import admin

from dogs.models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    ordering = ('pk',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'breed', 'owner')
    list_filter = ('breed',)
    ordering = ('name',)
