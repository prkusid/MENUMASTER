# Generated by Django 2.2.6 on 2019-11-21 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuSelection', '0015_auto_20191122_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuselection',
            name='type',
        ),
    ]
