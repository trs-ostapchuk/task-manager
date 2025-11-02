from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from tasks.models import Worker


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "home/worker_list.html"
