from django.urls import path

from tasks.views import (
    index,
    WorkerListView,
    WorkerDetailView,
    PositionListView,
    TaskListView
)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]

app_name = "tasks"
