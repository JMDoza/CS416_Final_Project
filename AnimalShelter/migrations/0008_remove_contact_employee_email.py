# Generated by Django 3.2.9 on 2021-12-07 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnimalShelter', '0007_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='employee_email',
        ),
    ]
