# Generated by Django 3.0.5 on 2020-05-02 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200502_1856'),
        ('reviews', '0010_auto_20200501_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='products.Product'),
        ),
    ]
