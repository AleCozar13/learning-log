"""Dependencies"""

from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    # Include default auth urls:
    path("", include("django.contrib.auth.urls")),
    # Registration pagel:
    path("register/", views.register, name="register"),
]
