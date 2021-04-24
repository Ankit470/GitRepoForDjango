from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    

    print(removepunc)
    print(djtext) 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
               analyzed = analyzed + char

        params = {'purpose':'Removed Puntuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To UpperCase','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params) 
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed = analyzed + char 
        params = {'purpose':'Removed New Line','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params) 
    if(spaceremover == "on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index + 1] ==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed New Line','analyzed_text':analyzed}
        
        # return render(request,'analyze.html',params) 
    
    
    if(removepunc !="on" and fullcaps !="on" and newlineremover !="on" and spaceremover != "on" ):
        return HttpResponse("Error")


    # else:
    #  return HttpResponse("Error")

    return render(request,'analyze.html',params)

