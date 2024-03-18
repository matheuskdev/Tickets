from rest_framework import generics
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    name = "category_list_create"
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = CategorySerializer

# TODO: Create views for delete Category.