from django.urls import path
from dogs.apps import DogsConfig
from django.views.decorators.cache import cache_page, never_cache

from dogs.views import index_view, BreedListView, DogBreedListView, DogListView, DogCreateView, DogDetailView, \
    DogUpdateView, DogDeleteView, DogDeactivatedListView, dog_toggle_activity, DogSearchListView, BreedSearchListView, \
    BreedDogSearchListView

app_name = DogsConfig.name

urlpatterns = [
    # breeds
    path('', cache_page(1)(index_view), name='index'),
    path('breeds/', cache_page(1)(BreedListView.as_view()), name='breeds'),
    path('breeds/search/', BreedSearchListView.as_view(), name='breed_search'),

    path('breeds/search_all/', BreedDogSearchListView.as_view(), name='breed_dog_search'),

    # dogs
    path('breeds/<int:pk>/dogs/', DogBreedListView.as_view(), name='breed_dogs'),
    path('dogs', DogListView.as_view(), name='dogs_list'),
    path('dogs/deactivated/', DogDeactivatedListView.as_view(), name='dogs_deactivated_list'),
    path('dogs/search/', DogSearchListView.as_view(), name='dogs_search'),

    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('dogs/update/<int:pk>/', never_cache(DogUpdateView.as_view()), name='dog_update'),
    path('dogs/toggle/<int:pk>/', dog_toggle_activity, name='dog_toggle_activity'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]
