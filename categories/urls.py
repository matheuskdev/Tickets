from django.urls import path
from . import views

urlpatterns = [
    path(
        'category/',
        views.CategoryListCreateView.as_view(),
        name=views.CategoryListCreateView.name
    ),
    # TODO: Create views for delete category.
]