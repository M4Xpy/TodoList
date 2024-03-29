from django.urls import path

from .views import (
    index,
    TagCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,

    TaskCreateView,
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
]

app_name = "tasks"
