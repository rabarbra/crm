# Generated by Django 2.1 on 2018-09-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metalware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastener',
            name='description',
            field=models.TextField(blank=True, help_text='Описание крепежного изделия'),
        ),
        migrations.AlterField(
            model_name='fastener',
            name='diametr',
            field=models.FloatField(blank=True, help_text='диаметр', null=True),
        ),
        migrations.AlterField(
            model_name='fastener',
            name='iso',
            field=models.CharField(blank=True, help_text='ISO', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fastener',
            name='length',
            field=models.FloatField(blank=True, help_text='длина', null=True),
        ),
        migrations.AlterField(
            model_name='fastener',
            name='sellers',
            field=models.TextField(blank=True, help_text='Поставщики, продавцы и магазины'),
        ),
        migrations.AlterField(
            model_name='fastener',
            name='thread',
            field=models.FloatField(blank=True, help_text='резьба', null=True),
        ),
    ]
