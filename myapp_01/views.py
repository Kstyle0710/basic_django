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

def download(request, pk):
    single = ImageBox.objects.get(pk=pk)
    return render(
        request,
        'myapp_01/download.html',
        {'single' : single}
    )