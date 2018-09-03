from django.forms import ModelForm
from .models import Fastener

class FastenerForm(ModelForm):
	class Meta:
		model = Fastener
		fields = ['type', 'thread', 'length', 'diametr', 'head', 'drive', 'coating', 'din', 'gost', 'iso', 'article', 'description', 'sellers']

#Добавить валидаторы