# Generated by Django 2.2.6 on 2019-11-21 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MenuSelection', '0010_auto_20191121_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipemaster',
            name='brand',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='receipemaster',
            name='type',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]