# Generated by Django 3.0.5 on 2023-04-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230419_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopmodel',
            name='Price',
            field=models.IntegerField(blank=True, verbose_name='price'),
        ),
    ]