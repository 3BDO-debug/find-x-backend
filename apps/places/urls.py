from django.urls import path
from . import handlers


urlpatterns = [
    path("places-data", handlers.places_handler),
    path("places-images-data", handlers.places_images_handler),
]
