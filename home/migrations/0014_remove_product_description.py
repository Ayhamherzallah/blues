# Generated by Django 4.1.7 on 2023-08-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_product_category_alter_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
