# Generated by Django 4.1.4 on 2023-01-12 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apartment',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]