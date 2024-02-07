from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Tag, Task


def index(request):
    return render(request, "tasks/index.html")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagListView(generic.ListView):
    model = Tag

    def get_queryset(self):
        return Tag.objects.prefetch_related(
            "tasks__tags",
        )


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/delete_tag.html"
    success_url = reverse_lazy("tasks:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")

