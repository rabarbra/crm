from django.shortcuts import render, get_object_or_404
from .models import Fastener
from .forms import FastenerForm

def catalog(request):
	#detail = get_object_or_404(Fastener, pk=pk)
	form = FastenerForm(request.POST)#, instance = detail)
	#if form.is_valid():
	#	detail = form.save(commit = False)
	#	detail.save()
	fasteners = Fastener.objects.all()
	return render(request, 'metalware/catalog.html', {'fasteners': fasteners, 'form':form})
