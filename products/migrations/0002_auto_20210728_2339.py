# Generated by Django 3.2.5 on 2021-07-28 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='price',
        ),
    ]
