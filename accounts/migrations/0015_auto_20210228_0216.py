# Generated by Django 3.1.7 on 2021-02-27 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210228_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone_number',
            new_name='phone',
        ),
    ]