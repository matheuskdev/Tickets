from rest_framework import generics
from rest_framework import permissions
from .models import Status
from .serializers import StatusSerializer

class StatusListCreateView(generics.ListCreateAPIView):
    name = "status_list_create"
    queryset = Status.objects.all()
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = StatusSerializer
