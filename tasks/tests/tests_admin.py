from django.test import TestCase
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Position, Task, TaskType
from tasks.admin import WorkerAdmin, PositionAdmin, TaskTypeAdmin, TaskAdmin


class AdminRegistrationTests(TestCase):
    """Tests that all models are correctly registered in Django admin."""

    def test_worker_registered(self):
        self.assertIn(Worker, admin.site._registry)
        self.assertIsInstance(admin.site._registry[Worker], WorkerAdmin)

    def test_position_registered(self):
        self.assertIn(Position, admin.site._registry)
        self.assertIsInstance(admin.site._registry[Position], PositionAdmin)

    def test_task_type_registered(self):
        self.assertIn(TaskType, admin.site._registry)
        self.assertIsInstance(admin.site._registry[TaskType], TaskTypeAdmin)

    def test_task_registered(self):
        self.assertIn(Task, admin.site._registry)
        self.assertIsInstance(admin.site._registry[Task], TaskAdmin)


class WorkerAdminTests(TestCase):
    """Tests for WorkerAdmin configuration."""

    def setUp(self):
        self.admin_class = WorkerAdmin(Worker, admin.site)

    def test_list_display(self):
        # WorkerAdmin extends UserAdmin.list_display
        for field in UserAdmin.list_display:
            self.assertIn(field, self.admin_class.list_display)

        self.assertIn("position", self.admin_class.list_display)

    def test_list_filter(self):
        self.assertEqual(self.admin_class.list_filter, ("position", "is_staff", "is_active"))

    def test_search_fields(self):
        self.assertEqual(self.admin_class.search_fields, ("username",))

    def test_ordering(self):
        self.assertEqual(self.admin_class.ordering, ("username",))

    def test_fieldsets_contains_position(self):
        # Ensure that fieldsets include "position"
        fields = [fs[1]["fields"] for fs in self.admin_class.fieldsets]
        flattened = [item for sublist in fields for item in sublist]
        self.assertIn("position", flattened)


class PositionAdminTests(TestCase):
    """Tests for PositionAdmin configuration."""

    def setUp(self):
        self.admin_class = PositionAdmin(Position, admin.site)

    def test_list_display(self):
        self.assertEqual(self.admin_class.list_display, ("name",))

    def test_search_fields(self):
        self.assertEqual(self.admin_class.search_fields, ("name",))


class TaskTypeAdminTests(TestCase):
    """Tests for TaskTypeAdmin configuration."""

    def setUp(self):
        self.admin_class = TaskTypeAdmin(TaskType, admin.site)

    def test_list_display(self):
        self.assertEqual(self.admin_class.list_display, ("name",))

    def test_search_fields(self):
        self.assertEqual(self.admin_class.search_fields, ("name",))


class TaskAdminTests(TestCase):
    """Tests for TaskAdmin configuration."""

    def setUp(self):
        self.admin_class = TaskAdmin(Task, admin.site)

    def test_list_display(self):
        expected = (
            "name", "deadline", "is_completed", "priority", "task_type"
        )
        self.assertEqual(self.admin_class.list_display, expected)

    def test_list_filter(self):
        self.assertEqual(self.admin_class.list_filter, ("priority", "task_type", "deadline"))

    def test_search_fields(self):
        self.assertEqual(self.admin_class.search_fields, ("name",))

    def test_ordering(self):
        self.assertEqual(self.admin_class.ordering, ("name",))
