# Generated by Django 3.2 on 2022-08-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20220809_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='brand',
            field=models.CharField(choices=[('fendi', 'fendi'), ('balenciaga', 'balenciaga')], max_length=40),
        ),
    ]