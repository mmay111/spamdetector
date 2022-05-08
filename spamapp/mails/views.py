from contextlib import nullcontext
from http.client import HTTPResponse
import pickle
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
#created views

model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

def index(request):
    name=request.POST.get('name')
    
    if request.method=="POST":
        
        data=[name]
        vec=cv.transform(data).toarray()
        result=model.predict(vec)
        if result[0]==0:
         #xx="This is Not A Spam Email"
            messages.success(request,"This is A Not Spam Email")
        else:
            messages.error(request,"This is A Spam Email")
        # xx="This is A Spam Email"

    context = {
        "name": name,
    }

    
    return render(request, "index.html",context)

def spams(request):

    return render(request, "spams.html")

def regular(request):

    return render(request, "regular.html")

