from django import forms
from django.forms import ModelForm, fields
from app.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'status', 'priority']