from django.shortcuts import render

# Create your views here.
from images.views import *
from .models import Project
from django.http import JsonResponse


def index(request):
    projects = Project.objects.all().prefetch_related('images_set')
    context = {
        'projects': projects
    }

    return render(request, 'index.html', context)

