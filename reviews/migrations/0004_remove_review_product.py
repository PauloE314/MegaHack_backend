# Generated by Django 3.0.5 on 2020-04-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
    ]
