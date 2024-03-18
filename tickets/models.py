from django.db import models
from departments.models import Department


class Ticket(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    file = models.FileField(upload_to='files/tickets/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Ticketss'
        db_table = 'ticket'
        db_table_comment = 'Tickets dos usuários do sistema.'
        indexes = [
            models.Index(fields=["title"], name="ticket_name_idx"),
        ]