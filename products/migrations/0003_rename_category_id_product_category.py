# Generated by Django 5.0.4 on 2024-05-09 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_category_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
