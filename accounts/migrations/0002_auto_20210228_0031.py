# Generated by Django 3.1.7 on 2021-02-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]