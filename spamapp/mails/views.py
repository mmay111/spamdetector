from contextlib import nullcontext
from http.client import HTTPResponse
from multiprocessing import context
import pickle
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
#created views

import pandas as pd


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
    data=pd.read_csv("spam.csv", encoding="latin-1")
    data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    data['class']=data['class'].map({'ham':0, 'spam':1})
    xx=data.loc[data['class'] == 0]

    xx = xx["message"]
    festival_list = xx.values.tolist()
    festival_list = festival_list[0:30]
    context={
        "festival_list":festival_list,
    }
    return render(request, "spams.html",context)

def regular(request):
    data=pd.read_csv("spam.csv", encoding="latin-1")
    data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    data['class']=data['class'].map({'ham':0, 'spam':1})
    xx=data.loc[data['class'] == 1]

    xx = xx["message"]
    festival_list = xx.values.tolist()
    festival_list = festival_list[0:30]
    context={
        "festival_list":festival_list,
    }
    return render(request, "regular.html",context)

