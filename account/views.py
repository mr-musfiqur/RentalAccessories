from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import CustomerProfile


@login_required
def profile(request):
    # pro_pic = request.CustomerProfile.profile_picture.url

    # return render(request, 'account/profile.html', {'pro_pic': pro_pic})
    return render(request, 'account/profile.html')

def register(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()


            # auto login
            username = registration_form.cleaned_data.get('username')
            password = registration_form.cleaned_data.get('password1')

            new_user = authenticate(username=username, password=password)
            login(request, new_user)

            # #profile row create
            # profile = Profile(user=new_user)
            # profile.save()

            return redirect('home')
        else:
            return render(request, 'account/register.html', {'form': registration_form})

    else:
        registration_form = RegistrationForm()
        context = {
            'form': registration_form
        }
        return render(request, 'account/register.html', context)
