from django.conf import settings
from django.core.mail import send_mail

def enquiry_email(subject, message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.ADMIN_EMAIL_ADDRESS]
    send_mail(subject, message, email_from, recipient_list)

def paid_email(email, subject, package_name, package_price, name, phone):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    admin_message = "Someone hass paid for a package. Here's the details\n\n Package Name: " + package_name + "\n Package Price: " + str(package_price) + "\n\n Details of the customer\n\n Name: " + name + "\n Email: " + email + "\n Phone: " + str(phone) + "\n\n with regards,\n\n your website"
    message = "Thank you for your payment. Your order is confirmed.Here's what you ordered\n\n Package Name: " + package_name + "\n Package Price: " + str(package_price) + "\n\n We will contact you soon."
    enquiry_email("Someone has paid for a package", admin_message)
    send_mail(subject, message, email_from, recipient_list)