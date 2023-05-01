from django.db import models

# Create your models here.
DURATION_CHOICES =[
    ("1/1", "1 Day and 1 Night"),
    ("1/2", "1 Day and 2 Night"),
    ("2/2", "2 Day and 2 Night"),
]
  

class Package(models.Model):
    name = models.CharField(max_length=50)
    dest_image = models.ImageField(upload_to='uploads')
    location = models.CharField(max_length=50)
    pack_image = models.ImageField(upload_to='uploads/')
    max_people = models.IntegerField(default=10)
    duration = models.CharField(max_length=20,choices=DURATION_CHOICES, default="1/1")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pack_desc_image = models.ImageField(upload_to='uploads/')
    pack_description = models.TextField()
    pack_includes = models.TextField()
    pack_services = models.TextField()

    def __str__(self):
        return self.name
