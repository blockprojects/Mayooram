from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^package/(?P<package_id>\d+)/?$', views.package, name='package description'),
    path('create/order', views.create_order_id, name='create_order_id'),
    path('contact', views.enquiry, name='contact'),
    path('success', views.success, name='success'),
]