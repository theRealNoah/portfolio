from django.urls import path
from . import views

urlpatterns = [
    path("", views.pdhelp_index, name="pdhelp_index")
]