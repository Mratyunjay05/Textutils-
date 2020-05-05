#i have created this file
from django.http import HttpResponse
from django.shortcuts import render 
# This code below which i have commented is for listing diffewrents urls on index page
# def index(request):
# 	return HttpResponse(''' This is about page and these are some of the  websites link given - <br>
# 		<a href="https://www.facebook.com/"> facebook </a> <br>
# 		<a href="https://mail.google.com/mail/?tab=rm&ogbl"> Gmail </a> <br>
# 		<a href="https://ieonline.microsoft.com/#ieslice"> Bing </a> <br>
# 		<a href="https://www.youtube.com/?gl=IN&tab=r1"> Youtube </a> <br>  ''')

# def about(request):
# 	return HttpResponse('this about page')
#   

def index(request):
	return render(request, 'index.html')
  #return HttpResponse('''<h1> Home </h1> <br> <a href="http://127.0.0.1:8000/removepunc">RemovePunc</a>''')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount','off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    
    if(fullcaps=="on"):
    	analyzed = ""
    	for char in djtext:
    		analyzed = analyzed+char.upper()
    	params = {'purpose': 'Captilize Text','analyzed_text' : analyzed}
    	djtext = analyzed
    	#return render(request,'analyze.html',params)

    if(newlineremover=="on"):
    	analyzed = ""
    	for char in djtext:
    		if char !="\n" and char !="\r":
    			analyzed = analyzed+char
    	params = {'purpose': 'New Line Removed','analyzed_text' : analyzed}
    	djtext = analyzed
    	#return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
    	analyzed = ""
    	for index,char in enumerate(djtext):
    		if not(djtext[index]==" " and djtext[index+1]==" ") :
    			analyzed = analyzed+char
    	params = {'purpose': 'Extra Space Removed','analyzed_text' : analyzed}
    	djtext = analyzed
    	#return render(request,'analyze.html',params)
    

    if(charcount=="on"):
    	analyzed = 0
    	for char in djtext:
    		if char !=" ":
    			analyzed = analyzed+1
    	params = {'purpose': 'Count The Character','analyzed_text' : analyzed}
    	djtext = analyzed
    	#return render(request,'analyze.html',params)

    if(charcount!="on" and extraspaceremover!="on" and newlineremover!="on" and removepunc != "on" and fullcaps!="on" ):
    	return HttpResponse("Please Select Any Function ! ^_^ ")

    return render(request,'analyze.html',params)
    
def capitalize(request):
	
	return HttpResponse('capitilize firstm letter')

def charcount(request):
	return HttpResponse('count the character')

	