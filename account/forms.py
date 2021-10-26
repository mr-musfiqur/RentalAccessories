from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)

    class Meta:
        model = User

        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',

                  ]


class CustomerProfile(UserCreationForm):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
    profile_pictures = forms.ImageField()

    class meta:
        model = User

        fields = ['first_name',
                  'last_name',
                  'email',
                  'image',
                  ]
