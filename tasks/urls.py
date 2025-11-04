from django.urls import path

from tasks.views import index, WorkerListView, WorkerDetailView, PositionListView

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("position/", PositionListView.as_view(), name="position-list"),
]

app_name = "tasks"
