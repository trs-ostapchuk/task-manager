from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker, Position, Task, TaskType


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Worker model

    Since add_fieldsets is not explicitly defined, Django uses fieldsets for both adding and editing a Worker.
    As a result, the "Add Worker" and "Edit Worker" pages display the same fields.
    This keeps the admin interface consistent and avoids the need to maintain two separate field configurations.
    """
    list_display = UserAdmin.list_display + ("position", )
    list_filter = ("position", "is_staff", "is_active")
    search_fields = ("username", )
    ordering = ("username", )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Additional info", {"fields": ("position", )}),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """
    Simple admin for managing position
    """
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    """
    Simple admin for managing position
    """
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Task model.
    """
    list_display = (
        "name", "deadline", "is_completed", "priority", "task_type"
    )
    list_filter = ("priority", "task_type", "deadline")
    search_fields = ("name", )
    ordering = ("name", )
