from django.contrib import admin
from .models import Cats, CatBreeds, Dogs, DogBreeds
# Register your models here.
admin.site.register(Cats)
admin.site.register(CatBreeds)
admin.site.register(Dogs)
admin.site.register(DogBreeds)
