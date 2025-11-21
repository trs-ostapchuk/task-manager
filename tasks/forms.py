from django.contrib.auth.forms import UserCreationForm
from django import forms
from tasks.models import Worker, Task, Position


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


class WorkerSearchForm(forms.Form):
    """
    Field for searching Worker
    """
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Search by username",
                "style": "width: 300px;",
            }
        )
    )


class TaskForm(forms.ModelForm):
    """Form for creating and updating tasks with styled widgets."""

    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "task_type": forms.Select(attrs={"class": "form-control"}),
            "assignees": forms.SelectMultiple(attrs={"class": "form-control"}),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class TaskSearchForm(forms.Form):
    """
    Field for searching Worker
    """
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Search by task",
                "style": "width: 300px;",
            }
        )
    )


class PositionForm(forms.ModelForm):
    """Form for creating and updating position with styled widgets."""

    class Meta:
        model = Position
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
