from django.urls import path
from . import handlers


urlpatterns = [
    path("register", handlers.register_handler),
    path("user-info", handlers.user_info_handler),
]
