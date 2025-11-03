from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from tasks.models import Worker


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "home/worker_list.html"

    def get_queryset(self):
        return Worker.objects.prefetch_related("tasks")


class WorkerDetailView(generic.DetailView):
    model = Worker
    template_name = "home/worker_detail.html"

    def get_context_data(self, **kwargs):
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
