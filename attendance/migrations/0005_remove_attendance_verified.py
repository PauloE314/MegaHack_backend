# Generated by Django 3.0.5 on 2020-05-01 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20200501_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='verified',
        ),
    ]
