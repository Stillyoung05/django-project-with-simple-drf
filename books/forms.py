from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import BooksModel


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        fields = ['book_name','short_description','publisher','book_image']

    def __init__(self, *args, **kwargs):
        super(UpdateBookForm, self).__init__(*args, **kwargs)