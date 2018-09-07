from django.forms import ModelForm
from .models import Fastener

class FastenerForm(ModelForm):
	class Meta:
		model = Fastener
		fields = ['id', 'type', 'head', 'drive', 'thread', 'length', 'diametr', 'coating', 'din', 'gost', 'iso', 'article']

#Добавить валидаторы