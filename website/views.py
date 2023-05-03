from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from .models import Package, Slide_Show_Images, Gallery_Images
import razorpay
import json
from .email_config import enquiry_email, paid_email

client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET))
client.set_app_details({"title" : "House Boat", "version" : "v0.0.1"})
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

@csrf_exempt
def create_order_id(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        amount = float(data['amount'])
        order = client.order.create({
            'amount': amount * 100, 
            'currency': 'INR', 
        })
        return JsonResponse({
            'success': True,
            'order': order,
        })

@csrf_exempt
def success(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        payment_id = request.POST.get('razorpay_payment_id')
        pay_details = client.payment.fetch(payment_id)
        pakage_name = pay_details['notes']['package_name']
        paid_email(pay_details['notes']['email'], "Payment Successful", pakage_name, pay_details['amount']/100, pay_details['notes']['name'], pay_details['notes']['phone'])
        return render(request, 'success.html')
    
@csrf_exempt
def enquiry(request):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            data = json.loads(data)
            enquiry_email(data['subject'], data['message'])
            return JsonResponse({
            'status': "success",
            })
        except Exception as e:
            return JsonResponse({"error":"true"})