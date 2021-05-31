from django.shortcuts import render

# Create your views here.
def about_index(request):
    return render(request, "about_index.html")


def home(request):
    return render(request, "home.html")

