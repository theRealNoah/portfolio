from django.shortcuts import render
from projects.models import  Project


# Create your views here.
# Function that makes a Django ORM Query to select all objects in the Project table
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


# Function that fetches the details of each project by primary key (pk)
# param: pk - id or primary key of the project
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
