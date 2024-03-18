from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        db_table = 'department'
        db_table_comment = 'Departamento dos usuários do sistema.'
        indexes = [
            models.Index(fields=["name"], name="department_name_idx"),
        ]
        unique_together = ["name"]