# Generated by Django 4.1.7 on 2023-03-20 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
    ]
