from django.test import TestCase
from django.urls import reverse
from tasks.models import Worker, Position, Task, TaskType
from django.utils import timezone


class WorkerTaskTests(TestCase):
    """
    Tests for Worker-related views and models.
    """

    def setUp(self):
        # Create positions
        self.position1 = Position.objects.create(name="Developer")
        self.position2 = Position.objects.create(name="Designer")

        # Create workers
        self.worker1 = Worker.objects.create_user(username="worker1", password="pass123", position=self.position1)
        self.worker2 = Worker.objects.create_user(username="worker2", password="pass123", position=self.position2)

        # Login as one worker to access protected views
        self.client.login(username="worker1", password="pass123")

    def test_worker_list_view(self):
        """
        Ensure WorkerListView returns a list of workers with correct table rendering.
        """
        url = reverse("tasks:worker-list")
        # Full list (no filter)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Table rows should contain both workers
        self.assertContains(response, '<td>worker1</td>', html=True)
        self.assertContains(response, '<td>worker2</td>', html=True)
        # Test search for worker2 only
        response = self.client.get(url, {"username": "worker2"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<td>worker2</td>', html=True)
        self.assertNotContains(response, '<td>worker1</td>', html=True)

    def test_worker_detail_view(self):
        """
        WorkerDetailView should return correct worker details including task stats.
        """
        url = reverse("tasks:worker-detail", args=[self.worker1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.worker1.username)
        self.assertContains(response, self.position1.name)


class PositionTaskTests(TestCase):
    """
    Tests for Position-related views and models.
    """

    def setUp(self):
        # Create positions
        self.position1 = Position.objects.create(name="Developer")
        self.position2 = Position.objects.create(name="Designer")

        # Create workers
        self.worker1 = Worker.objects.create_user(username="worker1", password="pass123", position=self.position1)
        self.worker2 = Worker.objects.create_user(username="worker2", password="pass123", position=self.position2)

        self.client.login(username="worker1", password="pass123")

    def test_position_list_view(self):
        """
        Ensure PositionListView renders all positions correctly.
        """
        url = reverse("tasks:position-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Developer")
        self.assertContains(response, "Designer")

    def test_position_detail_view(self):
        """
        PositionDetailView should return correct position info and list of workers.
        """
        url = reverse("tasks:position-detail", args=[self.position1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.position1.name)
        self.assertContains(response, self.worker1.username)
        self.assertNotContains(response, self.worker2.username)


class TaskTaskTests(TestCase):
    """
    Tests for Task-related views and models.
    """

    def setUp(self):
        # Create TaskTypes
        self.type1 = TaskType.objects.create(name="Bug Fix")
        self.type2 = TaskType.objects.create(name="Feature")

        # Create Tasks
        self.task1 = Task.objects.create(
            name="Fix login bug",
            description="Fix the login issue on homepage",
            deadline=timezone.now(),
            is_completed=True,
            priority="High",
            task_type=self.type1,
        )
        self.task2 = Task.objects.create(
            name="Add dashboard",
            description="Create dashboard page",
            deadline=timezone.now(),
            is_completed=False,
            priority="Urgent",
            task_type=self.type2,
        )

        # Create workers and assign tasks
        self.worker1 = Worker.objects.create_user(username="worker1", password="pass123")
        self.worker2 = Worker.objects.create_user(username="worker2", password="pass123")
        self.task1.assignees.add(self.worker1)
        self.task2.assignees.add(self.worker2)

        # Login for protected views
        self.client.login(username="worker1", password="pass123")

    def test_task_list_view(self):
        """
        TaskListView should render all tasks in the table.
        """
        url = reverse("tasks:task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix login bug")
        self.assertContains(response, "Add dashboard")

        # Test search functionality
        response = self.client.get(url, {"name": "dashboard"})
        self.assertContains(response, "Add dashboard")
        self.assertNotContains(response, "Fix login bug")

    def test_task_detail_view(self):
        """
        TaskDetailView should return correct task details.
        """
        url = reverse("tasks:task-detail", args=[self.task1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task1.task_type.name)
        self.assertContains(response, self.worker1.username)
