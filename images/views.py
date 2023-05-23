from django.shortcuts import render
from .models import Images


def show_images(r, id):
    return Images.objects.filter(project_id=id)
