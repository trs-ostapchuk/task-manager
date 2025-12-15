from django.test import TestCase
from tasks.forms import (
    WorkerCreationForm,
    WorkerUpdateForm,
    WorkerSearchForm,
    TaskForm,
    TaskSearchForm,
    PositionForm,
)
from tasks.models import Worker, Position, TaskType
from django.utils import timezone


class WorkerFormsTests(TestCase):
    """Tests for Worker creation, update, and search forms."""

    def setUp(self):
        self.position = Position.objects.create(name="Developer")

    def test_worker_creation_form_valid(self):
        """Ensure WorkerCreationForm is valid with proper data."""
        form_data = {
            "username": "john_doe",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "position": self.position.id,
            "password1": "complexpassword123",
            "password2": "complexpassword123",
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_creation_form_invalid_missing_fields(self):
        """Form should be invalid if required fields are missing."""
        form_data = {}
        form = WorkerCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("password1", form.errors)
        self.assertIn("password2", form.errors)

    def test_worker_update_form_valid(self):
        """Ensure WorkerUpdateForm is valid with proper data."""
        form_data = {
            "username": "jane_doe",
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com",
            "position": self.position.id,
        }
        form = WorkerUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_search_form(self):
        """WorkerSearchForm should accept optional username."""
        form = WorkerSearchForm(data={"username": "john"})
        self.assertTrue(form.is_valid())

        form_empty = WorkerSearchForm(data={})
        self.assertTrue(form_empty.is_valid())


class TaskFormsTests(TestCase):
    """Tests for Task creation and search forms."""

    def setUp(self):
        self.position = Position.objects.create(name="Tester")
        self.worker = Worker.objects.create_user(
            username="worker1", password="password", position=self.position
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")

    def test_task_form_valid(self):
        """TaskForm should be valid with correct data."""
        form_data = {
            "name": "Fix login bug",
            "description": "Users cannot log in.",
            "deadline": timezone.now(),
            "priority": "High",
            "task_type": self.task_type.id,
            "assignees": [self.worker.id],
            "is_completed": False,
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_missing_fields(self):
        """TaskForm should be invalid if required fields are missing."""
        form_data = {"name": ""}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_task_search_form(self):
        """TaskSearchForm should accept optional task name."""
        form = TaskSearchForm(data={"name": "Fix"})
        self.assertTrue(form.is_valid())

        form_empty = TaskSearchForm(data={})
        self.assertTrue(form_empty.is_valid())


class PositionFormsTests(TestCase):
    """Tests for Position creation and update forms."""

    def test_position_form_valid(self):
        """PositionForm should be valid with correct data."""
        form_data = {"name": "Manager"}
        form = PositionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_form_invalid_empty(self):
        """PositionForm should be invalid if name is empty."""
        form_data = {"name": ""}
        form = PositionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
