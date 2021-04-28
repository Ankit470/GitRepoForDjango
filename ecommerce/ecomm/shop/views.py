from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("we're at about")

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

