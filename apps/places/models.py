from django.db import models
import urllib
import os
from django.core.files import File

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=350, verbose_name="Place name")
    category = models.CharField(max_length=350, verbose_name="Place category")
    address = models.CharField(max_length=350, verbose_name="Address")
    description = models.TextField(verbose_name="Description")
    latitude = models.CharField(max_length=350, verbose_name="Place latitude")
    longitude = models.CharField(max_length=350, verbose_name="Place longitude")
    is_site_featured = models.BooleanField(
        default=True, verbose_name="Is site featured"
    )

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Place")
    image = models.ImageField(upload_to="uploads/places_imgs", null=True, blank=True)

    class Meta:
        verbose_name = "Place image"
        verbose_name_plural = "Place images"
