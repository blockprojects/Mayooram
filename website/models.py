from django.db import models

# Create your models here.
DURATION_CHOICES =[
    ("1D/1N", "1 Day and 1 Night"),
    ("1D/2N", "1 Day and 2 Night"),
    ("2D/2N", "2 Day and 2 Night"),
]
  

class Package(models.Model):
    name = models.CharField(max_length=50)
    dest_image = models.ImageField(upload_to='uploads/')
    location = models.CharField(max_length=50)
    pack_image = models.ImageField(upload_to='uploads/')
    max_people = models.IntegerField(default=10)
    duration = models.CharField(max_length=20,choices=DURATION_CHOICES, default="1/1")
    price = models.IntegerField(default=1000)
    pack_desc_image = models.ImageField(upload_to='uploads/')
    pack_description = models.TextField()
    pack_includes = models.TextField()
    pack_services = models.TextField()

    def save(self):
        day, night = self.duration.split('/')
        self.duration_text = f'{day.replace("D","")} Days/{night.replace("N","")} Nights'
        super().save()

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