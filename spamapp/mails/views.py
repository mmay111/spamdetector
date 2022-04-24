from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from mails.models import mails
# Create your views here.
#created views


#all, spam/ not spam ssyfalrını da ekle
def index(request):
    context = {
        "mails": mails.objects.all(),
        #"mails": mails.objects.filter(is_active=True),
        "xx": "Duyurular"  
    }
    
    return render(request, "index.html",context)

