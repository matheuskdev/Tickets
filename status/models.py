from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        db_table = 'status_ticket'
        db_table_comment = 'Status dos tickets do sistema.'
        indexes = [
            models.Index(fields=["name"], name="status_name_idx"),
        ]
        unique_together = ["name"]