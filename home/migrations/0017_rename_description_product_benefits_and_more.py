# Generated by Django 4.1.7 on 2023-08-10 15:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='benefits',
        ),
        migrations.AddField(
            model_name='product',
            name='ideal_for',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
