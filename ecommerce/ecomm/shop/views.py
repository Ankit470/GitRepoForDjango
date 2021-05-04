from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = { 'no_of_slides':nSlides ,'range':range(nSlides),'product':products}
    return render(request,'shop/index.html')

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

