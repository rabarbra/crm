from django.shortcuts import render
from .models import Fastener
from .forms import FastenerForm
from django.http import HttpResponseRedirect, HttpResponseNotFound

def catalog(request):
	fasteners = Fastener.objects.all()
	add_form = FastenerForm()
	forms = [FastenerForm(instance = i) for i in fasteners]
	if request.method == "POST":
		FastenerForm(request.POST).save()
		
	return render(request, 'metalware/catalog.html', {'fasteners': fasteners, 'forms': forms, 'add_form': add_form})

#def create(request):
#	if request.method == "POST":
#		detail = Fastener()
#		detail.