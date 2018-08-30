from django.db import models

class Fastener(models.Model):
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
		('LW', 'Locking washer'), #шайба стопорная (упорная) быстросъёмная
		('SW', 'Spring washer'), #шайба гроверная
	)
	type = models.CharField(max_length = 2, choices = TYPE_CHOICES, default = SC,)
	
	DIAMETR_CHOICES = (
		()
	)
	
	LENGTH_CHOICES = (
		()
	)
	
	MATERIAL_CHOICES = (
		()
	)
	
	STANDART_CHOICES = (
		()
	)