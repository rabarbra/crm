from django.db import models
from django.forms import ModelForm

class Fastener(models.Model): #таблица для крепежа
	
	TYPE_CHOICES = (
		('SC', 'Screw'), #винт
		('NU', 'Nut'), #гайка
		('FS', 'Flare-mount standoff'), #бонка, развальцовочная (резьбовая) втулка (бонка)
		('BN', 'Blind nut'), #бонка вытяжная, вытяжная гайка
		('BR', 'Blind rivet'), #заклепка вытяжная
		('SR', 'Solid rivet'), #заклёпка под молоток
		('SN', 'Swage nut'), #гайка запресовочная
		('WS', 'Welding stud'), #шпилька конденсаторная
		('TS', 'Threated welding stud'), #шпилька конденсаторная резьбовая
		('PS', 'Press-in stud'), #шпилька запресовочная
		('ST', 'Standoffs'), #втулка конденсаторная (для конденсаторной сварки)
		('PW', 'Plain washer'), #шайба
		('RW', 'Retaining washer'), #шайба стопорная (упорная) быстросъёмная
		('SW', 'Spring lock washer'), #шайба гроверная
	)
	
	DRIVE_CHOICES = (
		('SL', 'Slot'), #прямой (плоский)
		('CR', 'Cross'), #крестообразный с прорезью до края
		('PH', 'Phillips'), #филлипс: крестообразный, прорезь не доходит до края головки
		('PS', 'Phillips/Slotted'), #филипс + прямая прорезь
		('SQ', 'Square'), #квадратный
		('HE', 'Hex'), #шестиугольный
		('SP', 'Special'), #всякие другие странные шлицы
	)
	
	HEAD_CHOICES = (
		('CH', 'Cheese'), #цилиндрическая
		('RC', 'Raised cheese'), #полуцилиндрическая = цилиндрическая скруглённая, rased chees head = pan head, button, dome head
		('CS', 'Countersunk'), #потайная
		('RS', 'Raised countersunk'), #полупотайная, oval head
		('RO', 'Round'), #полукруглая
		('MU', 'Mushroom'), #полукруглая низкого профиля, большая полукруглая, truss head
		('TH', 'T-head'), #Т-образная
		('KG', 'Knurled grip'), #круглая (плоская) накатанная
		('SQ', 'Square'), #квадратная
		('SC', 'Square with collar'), #квадратная с выступом
		('HE', 'Hexagon'), #шестигранная
		('SP', 'Special'), #особая: все прочие необычные варианты головок
	)
	
	COATING_CHOICES = (
		('ZI', 'Zinc'), #цинк
		('SS', 'Stainless steel'), #нержавейка
		('OX', 'Oxidation'), #оксидирование
		('NI', 'Nickel'), #никель
		('AL', 'Aluminium'), #алюминий
		('WC', 'Without coating'), #без покрытия
	)
	
	type = models.CharField(max_length = 2, choices = TYPE_CHOICES, default = 'SC', help_text = "тип крепежа") #тип крепежа
	drive = models.CharField(max_length = 2, choices = DRIVE_CHOICES, null = True, blank = True, help_text = "шлиц") #шлиц
	head = models.CharField(max_length = 2, choices = HEAD_CHOICES, null = True, blank = True, help_text = "вид головки") #вид головки
	coating = models.CharField(max_length = 2, choices = COATING_CHOICES, default = 'WC', help_text = "покрытие, материал") #покрытие
	diametr = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True, help_text = "диаметр") #диаметр
	length = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True, help_text = "длина") #длина
	thread = models.DecimalField(max_digits = 5,  decimal_places = 2, null = True, blank = True, help_text = "резьба") #резьба
	din = models.PositiveSmallIntegerField(null = True, blank = True, help_text = "DIN") #DIN
	gost = models.CharField(max_length = 10, null = True, blank = True, help_text = "ГОСТ") #ГОСТ
	iso = models.CharField(max_length = 10, null = True, blank = True, help_text = "ISO") #ISO
	article = models.CharField(max_length = 20, null = True, blank = True, help_text = "Артикул") #Артикул
	description = models.TextField(blank = True, help_text = "Описание крепежного изделия") #Описание крепежного изделия
	sellers = models.TextField(blank = True, help_text = "Поставщики, продавцы и магазины") #Поставщики, продавцы и магазины (сделать потом как ManyToManyField на таблицу поставщиков)
	
	def __str__(self):
		return self.type+' DIN'+str(self.din) #доработать, чтобы выводилось полное название типа крепежа
		
	
	#ниже формы
	
	class FastenerForm(ModelForm):
		class Meta:
			model = Fastener
			fields = ['type', 'thread', 'length', 'diametr', 'head', 'drive', 'coating', 'din', 'gost', 'iso', 'article', 'descriptions']
	
#Добавить валидаторы
