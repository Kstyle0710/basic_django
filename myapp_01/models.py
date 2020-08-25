from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImageBox(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    upload_file = models.FileField(upload_to='file/%Y/%m/%d/', blank =True)
    image_1 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    image_2 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    image_3 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    image_4 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    image_5 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    image_6 = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


