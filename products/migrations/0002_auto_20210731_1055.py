# Generated by Django 3.2.5 on 2021-07-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='stripe_price_id',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='stripe_product_id',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
