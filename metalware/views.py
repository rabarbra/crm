from django.shortcuts import render

from django.shortcuts import render
from .models import Fastener
from .forms import FastenerForm

def catalog(request):
	form = FastenerForm()
	fasteners = Fastener.objects.all()
	return render(request, 'metalware/catalog.html', {'fasteners': fasteners, 'form':form})
