from django.urls import path

from dogs.urls import app_name, urlpatterns
from reviews.apps import ReviewsConfig

app_name = ReviewsConfig.name

urlpatterns = [

]