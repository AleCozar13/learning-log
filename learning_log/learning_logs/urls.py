"""Dependencies"""

from django.urls import path
from . import views

# Defines URL patterns for learning_logs:
app_name = "learning_logs"

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all topics.
    path("topis/", views.topics, name="topics"),
]
