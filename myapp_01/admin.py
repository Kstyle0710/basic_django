from django.contrib import admin
from .models import ImageBox
# Register your models here.

class ImageBoxAdin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'updated']


admin.site.register(ImageBox, ImageBoxAdin)