from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Worker


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
