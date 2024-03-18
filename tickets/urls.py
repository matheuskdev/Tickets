from django.urls import path
from . import views

urlpatterns = [
    path(
        'Ticket/',
        views.TicketListCreateView.as_view(),
        name=views.TicketListCreateView.name
    ),
    # TODO: Create views for delete deparment.
]