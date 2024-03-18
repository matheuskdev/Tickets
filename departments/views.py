from rest_framework import generics
from rest_framework import permissions
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    name = "department_list_create"
    queryset = Department.objects.all()
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = DepartmentSerializer

# TODO: Create views for delete Department.