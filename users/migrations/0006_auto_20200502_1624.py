# Generated by Django 3.0.5 on 2020-05-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='qt_votes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='score_sum',
        ),
    ]