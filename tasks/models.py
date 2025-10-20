from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    """
    Represents a single task in the Task Manager system.
    """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Position(models.Model):
    """
    Represents a position within the company.
    """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    """
    Represents a worker in the company.
    """
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
    )

    class Meta:
        ordering = ("username", )


class Task(models.Model):
    """
    Represents a single task assigned to one or more workers.
    """

    class Priority(models.TextChoices):
        URGENT = "Urgent", "Urgent"
        HIGH = "High", "High"
        MEDIUM = "Medium", "Medium"
        LOW = "Low", "Low"

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
    )

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} ({self.priority})"
