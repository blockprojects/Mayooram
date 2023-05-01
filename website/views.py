from django.shortcuts import render
from .models import Package
# Create your views here.

def home(request):
    return render(request, 'index.html')

def package(request):
    return HttpResponse('This is the package page.')