# Generated by Django 4.2.4 on 2023-08-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='rent_payed',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
