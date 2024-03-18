from django.urls import path
from . import views

urlpatterns = [
    path(
        'department/',
        views.DepartmentListCreateView.as_view(),
        name=views.DepartmentListCreateView.name
    ),
    # TODO: Create views for delete deparment.
]