# Generated by Django 4.1.4 on 2023-01-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='door_number',
            field=models.CharField(max_length=10),
        ),
    ]
