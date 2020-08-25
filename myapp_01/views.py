from django.shortcuts import render
from .models import ImageBox

# Create your views here.

def index(request):
    data = ImageBox.objects.all()
    return render(
        request,
        'myapp_01/index.html',
        {'data' : data}
    )

