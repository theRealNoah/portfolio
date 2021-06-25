from django.shortcuts import render


# Create your views here.
def pdhelp_index(request):
    return render(request, "pdhelp.html")
