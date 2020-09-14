from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BigBox(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    upload_file = models.FileField(upload_to='file/%Y/%m/%d/', blank =True)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created',]

class SmallBox(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    upload_file = models.FileField(upload_to='file/%Y/%m/%d/', blank =True)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank =True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bigone = models.ForeignKey(BigBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created',]

