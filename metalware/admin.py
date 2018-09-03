from django.contrib import admin

from .models import Fastener

class FastenerAdmin(admin.ModelAdmin):
	list_display = ('type', 'thread', 'length', 'diametr', 'head', 'drive', 'coating', 'din', 'gost', 'iso', 'article')
	list_filter = ('type', 'din', 'gost', 'iso', 'head', 'drive')
	fields = [('type', 'head', 'drive'), ('thread', 'length', 'diametr'), ('din', 'gost', 'iso', 'article'), 'description', 'sellers']
	
admin.site.register(Fastener, FastenerAdmin)
