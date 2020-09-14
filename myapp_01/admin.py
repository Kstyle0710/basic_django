from django.contrib import admin
from .models import BigBox, SmallBox
# Register your models here.

class BigBoxAdin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'updated']

class SmallBoxAdin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created', 'updated']


admin.site.register(BigBox, BigBoxAdin)
admin.site.register(SmallBox, SmallBoxAdin)