# Generated by Django 3.2.9 on 2021-12-07 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatBreeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_breed_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DogBreeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_breed_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('arrived', models.DateField(auto_now_add=True)),
                ('adopted', models.DateField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='images/dogs')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalShelter.dogbreeds')),
            ],
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('arrived', models.DateTimeField(auto_now_add=True)),
                ('adopted', models.DateTimeField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='images/cats')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimalShelter.catbreeds')),
            ],
        ),
    ]
