from django import forms
from django.forms import ModelForm
from .models import Category, Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ("task_name", "task_body", "category", "priority", "deadline")
        labels = {
            "task_name": "",
            "task_body": "",
            "category": "Category",
            "priority": "Priority",
            "deadline": "YYYY-MM-DD HH:MM:SS",
        }
        widgets = {
            "task_name": forms.TextInput(attrs={"class":"form-control", "placeholder": "Task Title"}),
            "task_body": forms.Textarea(attrs={"class":"form-control", "placeholder": "Task Detail"}),
            "category": forms.Select(attrs={"class":"form-control", "placeholder": "Category"}),
            "priority": forms.Select(attrs={"class":"form-control", "placeholder": "Priority"}),
            "deadline": forms.TextInput(attrs={"class":"form-control", "placeholder": "Deadline"}),
        }

