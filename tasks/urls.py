from django.urls import path

from .views import (
    index,
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,

    TaskCreateView,
    task_toggle,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("",
         index,
         name="index", ),
    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create", ),
    path("tags/",
         TagListView.as_view(),
         name="tag-list", ),
    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update", ),
    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete", ),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create", ),
    path('task/<int:pk>/toggle/',
         task_toggle,
         name='task-toggle'),
    path("tasks/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
]

app_name = "tasks"
