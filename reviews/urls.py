from django.urls import path

from dogs.urls import app_name, urlpatterns
from reviews.apps import ReviewsConfig

from reviews.views import ReviewListView, ReviewDeactivatedListView, ReviewDeactivatedListView

app_name = ReviewsConfig.name

urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews_list'),
    path('deactivated/', ReviewDeactivatedListView.as_view(), name='reviews_deactivated_list'),

]