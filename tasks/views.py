from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Tag


def index(request):
    return render(request, "tasks/index.html")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags:tag-list")
