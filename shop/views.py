from unicodedata import category
from shop.models import Product
from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
# Create your views here.

def index(request):
    # productData = Product.objects.all()

    
    # params = { 'no_of_slides':nSlides,'range':range(1,nSlides),'product':productData}
    # allProds=[[productData,range(1,nSlides),nSlides],
    #        [productData,range(1,nSlides),nSlides]]
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    print('category',cats)
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
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

def productView(request,id):
    product = Product.objects.filter(id=id)
    print(product)
    return render(request,'shop/productView.html',{'product':product[0]})

def checkout(request):
    return HttpResponse('This is checkout page')


