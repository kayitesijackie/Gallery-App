from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

