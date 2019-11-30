from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse 
from django.template import loader
from django.urls import reverse
import datetime 

from .models import (
	Dron,
	camara)
#from drones.models import (
#	Dron,
	#camara)
#def index(request):  
#   template = loader.get_template('index.html') # getting our template  
#   return render(request,'index.html')       # rendering the template in HttpResponse  
def dron_listing(request):
	drones= Dron.objects.all()

	lista=[]

	for index, dron in enumerate(drones):
		lista.append(
			{
				0:str(index +1),
				1:dron.modelo,
				2:dron.costo,
		    	'link': {
                	'url': reverse('dron', kwargs={
                    	'dron_id': dron.id
                	}),
                	'label': 'Detalle'
            	},
    		}
        )

	lista_data = {
		'lista': lista,
			'columnas': [
			    'No.', 'Modelo', 'Costo'
			]
	}    	

	context={
		'lista':lista_data,
	}
	template = loader.get_template('drones/dron_listing.html')
	return HttpResponse(template.render(context, request))
