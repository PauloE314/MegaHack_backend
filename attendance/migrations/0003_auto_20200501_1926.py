# Generated by Django 3.0.5 on 2020-05-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_attendance_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='verified_state',
            field=models.CharField(choices=[('UN', 'Ainda não respondido'), ('NO', 'Não atendido'), ('YES', 'Atendido')], max_length=3),
        ),
    ]
