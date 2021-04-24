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
    charactercounter = request.POST.get('charactercounter','off')

    print(removepunc)
    print(djtext) 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
               analyzed = analyzed + char

        params = {'purpose':'Removed Puntuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To UpperCase','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed = analyzed + char 
        params = {'purpose':'Removed New Line','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    elif(spaceremover == "on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index + 1] ==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed New Line','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 
    elif(charactercounter =="on"):
        analyzed = len(djtext)
        params = {'purpose':'Character Counter','analyzed_text':analyzed}
        return render(request,'analyze.html',params) 


    else:
     return HttpResponse("Error")

# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
    
#     return HttpResponse("charcount ")