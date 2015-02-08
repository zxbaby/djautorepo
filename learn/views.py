#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def fronthome(request):
    return render(request,'btadmin/index.html')

def index(request):
    if request.method == 'POST':
	form = AddForm(request.POST)
	if form.is_valid():
	    a = form.cleaned_data['a']
	    b = form.cleaned_data['b']
	    return HttpResponse(str(int(a)+int(b)))
    else:
	form = AddForm()
    return render(request,'learn/add.htm',{'form':form})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
