from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    profile_pic = CloudinaryField(verbose_name="Profile pic")
    address = models.CharField(max_length=350, verbose_name="Address")
    phone = models.CharField(max_length=350, verbose_name="Phone number")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
