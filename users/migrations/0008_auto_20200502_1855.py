# Generated by Django 3.0.5 on 2020-05-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_is_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=100),
        ),
    ]
