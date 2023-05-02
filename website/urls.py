from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('package/<int:package_id>/', views.package, name='about'),
]
