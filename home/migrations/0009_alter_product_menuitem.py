# Generated by Django 4.2.2 on 2023-07-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_product_price_productvariant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='menuitem',
            field=models.ManyToManyField(blank=True, to='home.menuitems'),
        ),
    ]
