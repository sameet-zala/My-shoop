# Generated by Django 3.1.7 on 2021-02-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210224_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='id',
        ),
    ]