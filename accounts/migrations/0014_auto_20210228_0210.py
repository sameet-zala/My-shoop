# Generated by Django 3.1.7 on 2021-02-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210228_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
