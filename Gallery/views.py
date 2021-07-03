from django.shortcuts import render
from .models import Image, Location


def index(request):
    images = Image.objects.all()
    return render(request, 'pictures/index.html',{'images': images[::-1]})
