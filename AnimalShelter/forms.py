from django import forms
from .models import Cats, CatBreeds, Dogs, DogBreeds, Contact


class CatBreedForm(forms.ModelForm):
    class Meta:
        model = CatBreeds
        fields = '__all__'


class DogBreedForm(forms.ModelForm):
    class Meta:
        model = DogBreeds
        fields = '__all__'


class CatForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        widgets = {
            'arrived': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'adopted': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class DogForm(forms.ModelForm):
    class Meta:
        model = Dogs
        fields = '__all__'
        widgets = {
            'arrived': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'adopted': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


class CatSearchForm(forms.ModelForm):
    age_less_than = forms.IntegerField(required=False)
    age_more_than = forms.IntegerField(required=False)

    class Meta:
        model = Cats
        fields = ['breed', 'gender']


class DogSearchForm(forms.ModelForm):
    age_less_than = forms.IntegerField(required=False)
    age_more_than = forms.IntegerField(required=False)

    class Meta:
        model = Dogs
        fields = ['breed', 'gender']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }
