from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='standard')
            user.groups.add(user_group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/register.html', {'form': form})


def login_view(request):
    valuenext = request.POST.get('next')
    print('TESTING: ', valuenext)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if valuenext == '':
                return redirect('index')
            else:
                return redirect(valuenext)


    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
