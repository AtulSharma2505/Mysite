from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext= request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    Capitalize = request.POST.get('Capitalize','off')
    lowercase = request.POST.get('lowercase','off')
    NewLineRemover = request.POST.get('NewLineRemover','off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover','off')

    if removepunc == "on":
       punctuations = '''.,;:!?'"-()[]{}<>/@#$%^&*~`|'''
       analyzed = ""
       for char in djtext:
           if char not in punctuations:
               analyzed = analyzed + char
       params = {'Purpose':'Removed punctuations', 'analyzed_text':analyzed}
       djtext = analyzed


    if (Capitalize == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'Purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if (lowercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'Purpose':'Changed to lowercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (NewLineRemover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'Purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        djtext = analyzed

    if (ExtraSpaceRemover == "on"):
        analyzed = ""
        djtext_length = len(djtext)
        for index, char in enumerate(djtext):
            if not (char == " " and index < djtext_length - 1 and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'Purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (
            removepunc != "on" and Capitalize != "on" and lowercase != "on" and NewLineRemover != "on" and ExtraSpaceRemover != "on"):
        return HttpResponse("Sorry! please select given operations.")

    return render(request, 'analyze.html',params)
