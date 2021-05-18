from django import forms
from .models import ToDo


class ToDoForms(forms.ModelForm):
    class Meta:
        model= ToDo
        fields= ['title']