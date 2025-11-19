from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import WorkerCreationForm, WorkerUpdateForm
from tasks.models import Worker, Position, Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    """
    Class-based view that displays a list of all workers.
    Uses the 'home/worker_list.html' template.
    """
    model = Worker
    template_name = "home/worker_list.html"
    paginate_by = 10

    def get_queryset(self):
        """
        Returns a queryset of all workers with their related tasks preloaded.
        Using `prefetch_related("tasks")` improves performance by avoiding
        the N+1 query problem when accessing each worker’s tasks.
        """
        return Worker.objects.prefetch_related("tasks")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Class-based view for displaying detailed information about a single worker.
    Shows basic info along with statistics about their assigned tasks.
    """
    model = Worker
    template_name = "home/worker_detail.html"

    def get_context_data(self, **kwargs):
        """
        Adds extra context variables to the template:
        - total_tasks: total number of tasks assigned to the worker
        - completed_tasks: how many tasks are completed
        - in_progress_tasks: how many are still in progress
        - completion_percent: percentage of completed tasks
        """
        context = super().get_context_data(**kwargs)
        worker = self.get_object()
        tasks = worker.tasks.all()
        total = tasks.count()
        completed = tasks.filter(is_completed=True).count()
        in_progress = total - completed
        completion_percent = int((completed / total) * 100) if total > 0 else 0

        context.update({
            "total_tasks": total,
            "completed_tasks": completed,
            "in_progress_tasks": in_progress,
            "completion_percent": completion_percent,
        })

        return context


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Allows authenticated users to create a new worker.
    Redirects to the worker list after successful creation.
    """
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("tasks:worker-list")
    template_name = "home/worker_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Allows editing of an existing worker's profile.
    """
    model = Worker
    form_class = WorkerUpdateForm
    template_name = "home/worker_form.html"
    success_url = reverse_lazy("home:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    """
    Class-based view that displays a list of all position.
    Uses the 'home/position_list.html' template.
    """
    model = Position
    template_name = "home/position_list.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    """
    Class-based view that displays a list of all tasks.
    Uses the 'home/task_list.html' template.
    """
    model = Task
    template_name = "home/task_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.select_related("task_type").prefetch_related("assignees")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Class-based view that displays a detail of task.
    Uses the 'home/task_detail.html' template.
    """
    model = Task
    template_name = "home/task_detail.html"
