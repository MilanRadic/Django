# Generated by Django 3.2.5 on 2021-07-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpad', '0003_auto_20210706_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='gtin',
            field=models.PositiveIntegerField(blank=True, default='0', max_length=100, verbose_name='gtin'),
        ),
        migrations.AlterField(
            model_name='device',
            name='weight_of_the_device',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
    ]
