from django import forms
from .models import CustomUser
from django.forms.utils import ErrorList


class NameForm(forms.ModelForm):
    CHOICES = (
        ('SCIENCE', 'SCIENCE'),
        ('ART', 'ART'),
    )

    classes = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'placeholder': 'Select a class'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'classes')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }

        labels = {
            'username': False,
            'password': False,
        }


