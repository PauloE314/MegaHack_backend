# Generated by Django 3.0.5 on 2020-04-29 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200429_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='score',
        ),
    ]
