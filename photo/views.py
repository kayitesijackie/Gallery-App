from django.shortcuts import render,redirect
from .models import Image,Category,Location
from django.http import Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

def display_location(request,location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images,'locations':locations})


