from django.db import models

# Create your models here.

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CatBreeds(models.Model):
    cat_breed_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_breed_name


class DogBreeds(models.Model):
    dog_breed_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dog_breed_name


class Cats(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    breed = models.ForeignKey(CatBreeds, on_delete=models.CASCADE, blank=True)
    age = models.IntegerField()
    description = models.TextField()
    arrived = models.DateTimeField(auto_now_add=True, blank=True)
    adopted = models.DateTimeField(null=True, blank=True)
    img = models.ImageField(upload_to='images/cats')

    def __str__(self):
        return self.name


class Dogs(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    breed = models.ForeignKey(DogBreeds, on_delete=models.CASCADE, blank=True)
    age = models.IntegerField()
    description = models.TextField()
    arrived = models.DateField(auto_now_add=True, blank=True)
    adopted = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to='images/dogs')

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    user_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
