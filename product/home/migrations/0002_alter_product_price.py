# Generated by Django 3.2.11 on 2023-02-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
