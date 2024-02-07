from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from tasks.models import Tag, Task


def index(request):
    return render(request,
                  "tasks/index.html",
                  {'tasks': Task.objects.prefetch_related('tags')})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))


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
