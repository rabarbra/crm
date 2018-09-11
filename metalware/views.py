from django.shortcuts import render
from .models import Fastener
from .forms import FastenerForm
from django.http import HttpResponseRedirect, HttpResponseNotFound

def catalog(request):
	add_form = FastenerForm()
	order = request.GET.get("o", "")
	if order == '':
		order = 'id'
	fasteners = Fastener.objects.order_by(order)
	if request.method == "POST":
		detail = FastenerForm(request.POST)
		detail.save()
	return render(request, 'metalware/catalog.html', {'fasteners': fasteners, 'add_form': add_form})
	
def delete(request, id):
	try:
		detail = Fastener.objects.get(id=id)
		detail.delete()
		return HttpResponseRedirect("/catalog")
	except Fastener.DoesNotExist:
		return HttpResponseRedirect("/catalog")
		
def edit(request, id):
	try:
		edit_detail = Fastener.objects.get(id=id)
		edit_form = FastenerForm(instance = edit_detail)
		if request.method == "POST":
			edited_detail = FastenerForm(request.POST, instance = edit_detail)
			edited_detail.save()
			return HttpResponseRedirect("/catalog")
		return render(request, 'metalware/edit.html', {'edit_form': edit_form})
	except Fastener.DoesNotExist:
		return HttpResponseNotFound("Detail not found")