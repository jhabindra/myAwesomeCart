from shop.models import Product
from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
# Create your views here.

def index(request):
    productData = Product.objects.all()

    n = len(productData)
    nSlides = n//4 + ceil((n/4)-(n//4))
    # params = { 'no_of_slides':nSlides,'range':range(1,nSlides),'product':productData}
    allProds=[[productData,range(1,nSlides),nSlides],
           [productData,range(1,nSlides),nSlides]]
    params = {'allProds':allProds}

    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

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


