from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = { 'no_of_slides':nSlides ,'range':range(1,nSlides),'product':products}
    #Demo Prod List !
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    allProds =[]
    catprod = Product.objects.values('category','id')
    #Set Comprehension
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
         
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("we're at contact")

def tracker(request):
    return HttpResponse("we're at tracker")

def search(request):
    return HttpResponse("we're at search")

def productView(request):
    return HttpResponse("we're at product view")

def checkout(request):
    return HttpResponse("we're at checkout")

