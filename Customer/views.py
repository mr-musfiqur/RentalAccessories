from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request,'account/profile.html')