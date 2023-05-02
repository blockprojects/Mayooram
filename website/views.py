from django.shortcuts import render
from .models import Package, Slide_Show_Images, Gallery_Images
# Create your views here.

def home(request):
    packages = Package.objects.all()
    slideshow = Slide_Show_Images.objects.all()
    gallery = Gallery_Images.objects.all()
    for package in packages:
        day, night = package.duration.split('/')
        package.duration_txt = f'{day.replace("D","")} Days/{night.replace("N","")} Nights'
    return render(request, 'index.html', {'packages': packages, 'slideshow': slideshow, 'gallery': gallery})

def package(request, package_id):
    pack = Package.objects.get(id=package_id)
    pack.pack_services = pack.pack_services.split('\n')
    return render(request, 'package.html', {'package': pack})