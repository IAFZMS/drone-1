from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse 
import datetime 

#def index(request):  
#   template = loader.get_template('index.html') # getting our template  
#   return render(request,'index.html')       # rendering the template in HttpResponse  
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
	return render(request,'index.html')

