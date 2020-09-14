from django.shortcuts import render
from .models import BigBox, SmallBox

# Create your views here.

def index(request):
    bigdata = BigBox.objects.all()
    return render(
        request,
        'myapp_01/index.html',
        {'bigdata' : bigdata}
    )

def download(request, pk):
    single = BigBox.objects.get(pk=pk)
    return render(
        request,
        'myapp_01/download.html',
        {'single' : single}
    )

def samll_index(request):
    smalldata = SmallBox.objects.all()
    return render(
        request,
        'myapp_01/small_index.html',
        {'smalldata' : smalldata}
    )