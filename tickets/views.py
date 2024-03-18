from rest_framework import generics
from rest_framework import permissions
from .models import Ticket
#from .serializers import TicketSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    name = "ticket_list_create"
# TODO: Create views for delete Ticket.