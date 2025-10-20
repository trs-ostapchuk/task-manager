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
