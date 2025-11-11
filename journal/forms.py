# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DailyEntry, DailyTask


class DailyEntryForm(forms.ModelForm):
    # Entry form
    class Meta:
        model = DailyEntry
        fields = ['date', 'title', 'content', 'mood']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entry title...'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Write about your day...'}),
            'mood': forms.Select(attrs={'class': 'form-select'}),
        }


class DailyTaskForm(forms.ModelForm):
    # Task form
    class Meta:
        model = DailyTask
        fields = ['title', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task description...'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UserRegisterForm(UserCreationForm):
    # Registration form
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'