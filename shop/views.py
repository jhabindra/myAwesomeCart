from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('This is about page')

def contact(request):
    return HttpResponse('This is contact page')


def tracker(request):
    return HttpResponse('This is tracker page')



def search(request):
    return HttpResponse('This is search page')

def prodView(request):
    return HttpResponse('This is prodview page')

def checkout(request):
    return HttpResponse('This is checkout page')


