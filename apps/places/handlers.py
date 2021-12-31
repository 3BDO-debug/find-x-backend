import requests
import json
import tempfile
from django.http import HttpResponse
from django.core import files
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


# Create your views here.
def inject_db(request):
    places_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=weeding places in egypt &key=AIzaSyCmVsZMzkCcz1JkdVzEeN4BIdrXas0dTec"
    places_request = requests.get(url=places_url)
    places = json.loads(places_request.text)

    for place in places.get("results"):
        place_id = place.get("place_id")
        place_details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key=AIzaSyCmVsZMzkCcz1JkdVzEeN4BIdrXas0dTec"
        place_details_request = requests.get(url=place_details_url)
        created_place = models.Place.objects.create(
            name=place.get("name"),
            category="weeding-hall",
            address=place.get("formatted_address"),
            description="This is a featured place by the site admin, which means that it had been scraped from google maps API with no description, if you have a description for this place please feel free to contact site admin to help us grow and collect more data.",
            latitude=place.get("geometry").get("location").get("lat"),
            longitude=place.get("geometry").get("location").get("lng"),
        )
        place_details_request_data = json.loads(place_details_request.text)
        try:
            for image in place_details_request_data.get("result").get("photos"):
                image_ref = image.get("photo_reference")
                image_api_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={image_ref}&key=AIzaSyCmVsZMzkCcz1JkdVzEeN4BIdrXas0dTec"
                image_api_request = requests.get(url=image_api_url)
                lf = tempfile.NamedTemporaryFile()
                file_name = f"place_name_{created_place.name}.png"
                for block in image_api_request.iter_content(1024 * 8):

                    # If no more file then stop
                    if not block:
                        break

                    # Write image block to temporary file
                    lf.write(block)

                created_place_image = models.PlaceImage.objects.create(
                    place=created_place
                )
                created_place_image.image.save(file_name, files.File(lf))
        except:
            pass

    return HttpResponse("hello")


@api_view(["GET", "POST"])
@permission_classes([])
@authentication_classes([])
def places_handler(request):

    if request.method == "POST" and request.user.is_authenticated:
        pass

    places = models.Place.objects.all()
    places_serializer = serializers.PlaceSerializer(places, many=True)

    return Response(status=status.HTTP_200_OK, data=places_serializer.data)


@api_view(["GET", "POST"])
def places_images_handler(request):

    if request.method == "POST" and request.user.is_authenticated:
        pass

    places_images = models.PlaceImage.objects.all()
    places_images_serializer = serializers.PlaceImageSerializer(
        places_images, many=True
    )

    return Response(status=status.HTTP_200_OK, data=places_images_serializer.data)
