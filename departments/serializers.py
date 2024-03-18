from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

# TODO: Create serializer for delete Department.