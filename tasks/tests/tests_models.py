from django.test import TestCase

from tasks.models import TaskType, Position, Worker, Task


class ModelsTests(TestCase):

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="test")
        self.assertEqual(str(task_type), task_type.name)

    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), position.name)

    def test_worker_str(self):
        worker = Worker.objects.create(
            username="test",
            password="pass12345",
            first_name="first_test",
            last_name="last_test",
        )
        self.assertEqual(str(worker), f"{worker.first_name} {worker.last_name} ({worker.username})")

    def test_task_str(self):
        task_type = TaskType.objects.create(name="test")
        task = Task.objects.create(
            name="FixTests",
            description="Fixing tests",
            priority=Task.Priority.HIGH,
            task_type=task_type,
        )
        self.assertEqual(str(task), f"{task.name} ({task.priority})")
