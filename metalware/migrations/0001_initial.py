# Generated by Django 2.1 on 2018-08-31 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fastener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SC', 'Screw'), ('NU', 'Nut'), ('FS', 'Flare-mount standoff'), ('BN', 'Blind nut'), ('BR', 'Blind rivet'), ('SR', 'Solid rivet'), ('SN', 'Swage nut'), ('WS', 'Welding stud'), ('TS', 'Threated welding stud'), ('PS', 'Press-in stud'), ('ST', 'Standoffs'), ('PW', 'Plain washer'), ('RW', 'Retaining washer'), ('SW', 'Spring lock washer')], default='SC', help_text='тип крепежа', max_length=2)),
                ('drive', models.CharField(blank=True, choices=[('SL', 'Slot'), ('CR', 'Cross'), ('PH', 'Phillips'), ('PS', 'Phillips/Slotted'), ('SQ', 'Square'), ('HE', 'Hex'), ('SP', 'Special')], help_text='шлиц', max_length=2, null=True)),
                ('head', models.CharField(blank=True, choices=[('CH', 'Cheese'), ('RC', 'Raised cheese'), ('CS', 'Countersunk'), ('RS', 'Raised countersunk'), ('RO', 'Round'), ('MU', 'Mushroom'), ('TH', 'T-head'), ('KG', 'Knurled grip'), ('SQ', 'Square'), ('SC', 'Square with collar'), ('HE', 'Hexagon'), ('SP', 'Special')], help_text='вид головки', max_length=2, null=True)),
                ('coating', models.CharField(choices=[('ZI', 'Zinc'), ('SS', 'Stainless steel'), ('OX', 'Oxidation'), ('NI', 'Nickel'), ('AL', 'Aluminium'), ('WC', 'Without coating')], default='WC', help_text='покрытие, материал', max_length=2)),
                ('diametr', models.DecimalField(blank=True, decimal_places=2, help_text='диаметр', max_digits=5, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, help_text='длина', max_digits=5, null=True)),
                ('thread', models.DecimalField(blank=True, decimal_places=2, help_text='резьба', max_digits=5, null=True)),
                ('din', models.PositiveSmallIntegerField(blank=True, help_text='DIN', null=True)),
                ('gost', models.CharField(blank=True, help_text='ГОСТ', max_length=10, null=True)),
                ('iso', models.PositiveSmallIntegerField(blank=True, help_text='ISO', null=True)),
                ('article', models.CharField(blank=True, help_text='Артикул', max_length=20, null=True)),
                ('description', models.TextField(help_text='Описание крепежного изделия')),
                ('sellers', models.TextField(help_text='Поставщики, продавцы и магазины')),
            ],
        ),
    ]