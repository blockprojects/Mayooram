from django.db import models

# Create your models here.

"""
To add new choice use the same format and it as tuple in the list, day/night should be the format

"""
DURATION_CHOICES =[
    ("1D/1N", "1 Day and 1 Night"),
    ("1D/2N", "1 Day and 2 Night"),
    ("2D/2N", "2 Day and 2 Night"),
]
  

class Package(models.Model):
    name = models.CharField(max_length=50, help_text="Enter Package Name <em>(max 50 characters)</em>")
    dest_image = models.ImageField(upload_to='uploads/', help_text="This would show up in Destination section of home page")
    location = models.CharField(max_length=50)
    pack_image = models.ImageField(upload_to='uploads/',  help_text="This would show up in Package section of home page")
    max_people = models.IntegerField(default=10)
    duration = models.CharField(max_length=20,choices=DURATION_CHOICES, default="1/1")
    price = models.IntegerField(default=1000, help_text="Price per person in INR <strong>doesn't support decimal values</strong>")
    pack_desc_image = models.ImageField(upload_to='uploads/', help_text="This would show up in Package Description section of package page")
    pack_description = models.TextField(help_text="Just press Enter to add a linebreak")
    pack_includes = models.TextField(help_text="Just press Enter to add a linebreak")
    pack_services = models.TextField(help_text="<strong>Enter every service on a new line</strong>")

    def __str__(self):
        return self.name

class Slide_Show_Images(models.Model):
    image = models.ImageField(upload_to='slideshow/')
    alternate_tag = models.CharField(max_length=50, default="Slide Show Image")

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name_plural = "Slide Show Images"
    
class Gallery_Images(models.Model):
    image = models.ImageField(upload_to='gallery/')
    alternate_tag = models.CharField(max_length=50, default="Gallery Image")

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name_plural = "Gallery Images"