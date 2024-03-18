from django.urls import path
from . import views

urlpatterns = [
    path(
        'status/',
        views.StatusListCreateView.as_view(),
        name=views.StatusListCreateView.name
    ),
    # TODO: Create views for delete status
]