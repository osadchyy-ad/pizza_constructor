# Generated by Django 2.1.7 on 2019-03-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_auto_20190308_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.FloatField(),
        ),
    ]
