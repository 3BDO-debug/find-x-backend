from rest_framework.serializers import ModelSerializer
from . import models


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = models.Place
        fields = "__all__"


class PlaceImageSerializer(ModelSerializer):
    class Meta:
        model = models.PlaceImage
        fields = "__all__"
