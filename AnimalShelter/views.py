from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Cats, CatBreeds, Dogs, DogBreeds
from .forms import CatBreedForm, CatForm, DogBreedForm, DogForm, CatSearchForm, DogSearchForm, ContactForm

# Create your views here.


def index(request):
    feat_1 = Dogs.objects.get(id=2)
    feat_2 = Cats.objects.get(id=2)
    feat_3 = Dogs.objects.get(id=5)
    context = {
        'feat_1': feat_1,
        'feat_2': feat_2,
        'feat_3': feat_3,
    }
    return render(request, 'AnimalShelter/index.html', context)


def about(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'AnimalShelter/about_us.html')
    return render(request, 'AnimalShelter/about_us.html', {'form': form})


def find(request):
    return render(request, 'AnimalShelter/find.html')


@permission_required('AnimalShelter.view_dogs', login_url='login')
def dog_search(request):
    form = DogSearchForm(request.POST or None, request.FILES or None)
    pets = None
    database = 'dogs'
    context = {
        'form': form,
        'pets': pets,
        'database': database,
    }

    if request.method == 'POST':
        if form.is_valid():
            breed = form.cleaned_data['breed']
            gender = form.cleaned_data['gender']
            more = form.cleaned_data['age_more_than']
            less = form.cleaned_data['age_less_than']

            qs = Dogs.objects.all()
            if breed:
                qs = qs.filter(breed=breed)
                print(breed)
            if gender:
                qs = qs.filter(gender=gender)
                print(gender)
            if more:
                qs = qs.filter(age__gte=more)
                print(more)
            if less:
                qs = qs.filter(age__lte=less)
                print(less)

            context['pets'] = qs
            return render(request, 'AnimalShelter/pet_search.html', context)
    return render(request, 'AnimalShelter/pet_search.html', context)


@permission_required('AnimalShelter.view_cats', login_url='login')
def cat_search(request):
    form = CatSearchForm(request.POST or None)
    pets = None
    database = 'cats'
    context = {
        'form': form,
        'pets': pets,
        'database': database,
    }

    if request.method == 'POST':
        if form.is_valid():
            breed = form.cleaned_data['breed']
            gender = form.cleaned_data['gender']
            more = form.cleaned_data['age_more_than']
            less = form.cleaned_data['age_less_than']
            qs = Cats.objects.all()
            if breed:
                qs = qs.filter(breed=breed)
                # print(breed)
            if gender:
                qs = qs.filter(gender=gender)
                # print(gender)
            if more:
                qs = qs.filter(age__gte=more)
                # print(more)
            if less:
                qs = qs.filter(age__lte=less)
                # print(less)

            context['pets'] = qs
            return render(request, 'AnimalShelter/pet_search.html', context)
    return render(request, 'AnimalShelter/pet_search.html', context)


@permission_required('AnimalShelter.view_cats', login_url='login')
def profile_cat(request, id):
    pet = Cats.objects.get(id=id)
    return render(request, 'AnimalShelter/pet_profile.html', {'pet': pet})


@permission_required('AnimalShelter.view_dogs', login_url='login')
def profile_dog(request, id):
    pet = Dogs.objects.get(id=id)
    return render(request, 'AnimalShelter/pet_profile.html', {'pet': pet})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def dashboard(request):
    cats = Cats.objects.all()
    dogs = Dogs.objects.all()
    cbreeds = CatBreeds.objects.all()
    dbreeds = DogBreeds.objects.all()

    context = {
        'cats': cats,
        'dogs': dogs,
        'cbreeds': cbreeds,
        'dbreeds': dbreeds,
    }
    return render(request, 'CRUD/dashboard.html', context)


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def create_cat(request):
    form = CatForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def create_dog(request):
    form = DogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def create_cbreed(request):
    form = CatBreedForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def create_dbreed(request):
    form = DogBreedForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def update_cat(request, id):
    cat = Cats.objects.get(id=id)
    print('test1', cat)
    form = CatForm(request.POST or None, instance=cat)

    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def update_dog(request, id):
    dog = Dogs.objects.get(id=id)
    form = DogForm(request.POST or None, instance=dog)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def update_cbreed(request, id):
    cbreed = CatBreeds.objects.get(id=id)
    form = CatBreedForm(request.POST or None, instance=cbreed)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def update_dbreed(request, id):
    dbreed = DogBreeds.objects.get(id=id)

    form = CatForm(request.POST or None, instance=dbreed)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'CRUD/object_form.html', {'form': form})


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def delete_cat(request, id):
    item = Cats.objects.get(id=id)
    database = 'cats'

    context = {
        'item': item,
        'database': database
    }

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'CRUD/object_delete.html', context)


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def delete_dog(request, id):
    item = Dogs.objects.get(id=id)
    database = 'dogs'
    context = {
        'item': item,
        'database': database
    }

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'CRUD/object_delete.html', context)


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def delete_dbreed(request, id):
    item = DogBreeds.objects.get(id=id)
    database = 'dbreed'

    context = {
        'item': item,
        'database': database
    }
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'CRUD/object_delete.html', context)


@permission_required(['AnimalShelter.change_dogs', 'AnimalShelter.change_cats'], login_url='login')
def delete_cbreed(request, id):
    item = CatBreeds.objects.get(id=id)
    database = 'cbreed'

    context = {
        'item': item,
        'database': database
    }

    if request.method == 'POST':
        item.delete()
        # after deleting redirect to view_product page
        return redirect('dashboard')

    # if the request is not post, render the page with the product's info
    return render(request, 'CRUD/object_delete.html', context)
