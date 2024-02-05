from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')
    # user_image = forms.ImageField(required=False)  # Add this line for the user image field

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','user_image','phone')


        