# Generated by Django 3.0.5 on 2020-05-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20200502_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='score',
            new_name='attendant_score',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='verified_state',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendant_vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='client_vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='client_score',
            field=models.IntegerField(default=3, null=True),
        ),
    ]