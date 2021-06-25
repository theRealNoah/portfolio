from django.urls import path
from . import views

urlpatterns = [
    path("", views.timeline_index, name="timeline_index")
]