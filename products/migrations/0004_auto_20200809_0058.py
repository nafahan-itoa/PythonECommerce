# Generated by Django 3.1 on 2020-08-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='', null=True, upload_to='products/images'),
        ),
    ]
