from django.shortcuts import render
from .models import Fastener
from .forms import FastenerForm
from django.http import HttpResponseRedirect, HttpResponseNotFound

def catalog(request):
	fasteners = Fastener.objects.all()
	add_form = FastenerForm()
	forms = [FastenerForm(instance = i) for i in fasteners]
	if request.method == "POST":
		detail = FastenerForm(request.POST)
		try:
			detail.instance.delete()
		except:
			pass
		detail.save()
		#FastenerForm(request.POST).save()
		
	return render(request, 'metalware/catalog.html', {'fasteners': fasteners, 'forms': forms, 'add_form': add_form})

def delete(request, id):
	try:
		detail = Fastener.objects.get(id=id)
		detail.delete()
		return HttpResponseRedirect("/catalog")
	except Fastener.DoesNotExist:
		return HttpResponseRedirect("/catalog")
		
#def edit(request, id):
#	try:
#		detail = Fastener.objects.get(id=id)
#		
#		if request.method == "POST":
#			detail = FastenerForm(request.POST)
#			detail.save()
#			return HttpResponseRedirect("/catalog")
#	except Fastener.DoesNotExist:
#		return HttpResponseNotFound("Detail not found")

#def create(request):
#	if request.method == "POST":
#		detail = Fastener()
#		detail.
