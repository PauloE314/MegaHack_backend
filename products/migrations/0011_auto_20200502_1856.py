# Generated by Django 3.0.5 on 2020-05-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url_image',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]