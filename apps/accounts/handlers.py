from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def register_handler(request):
    models.User.objects.create_user(
        profile_pic=request.data.get("profilePic"),
        first_name=request.data.get("firstname"),
        last_name=request.data.get("lastname"),
        email=request.data.get("email"),
        username=request.data.get("username"),
        phone=request.data.get("phone"),
        address=request.data.get("address"),
        password=request.data.get("password"),
    )

    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def user_info_handler(request):
    user = models.User.objects.get(id=request.user.id)
    user_serializer = serializers.UserSerializer(user, many=False)
    return Response(status=status.HTTP_200_OK, data=user_serializer.data)
