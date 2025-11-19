from django.contrib.auth.forms import UserCreationForm
from django import forms
from tasks.models import Worker


class WorkerCreationForm(UserCreationForm):
    """
    Form for creating new Worker instances (custom user model).
    Inherits from Django's UserCreationForm to handle passwords securely.
    """

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-select"}),
        }


class WorkerUpdateForm(forms.ModelForm):
    """
    Form for editing Worker (custom user model) without password fields.
    """
    class Meta:
        model = Worker
        fields = ("username", "first_name", "last_name", "email", "position")

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-select"}),
        }
