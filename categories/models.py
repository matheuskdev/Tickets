from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
        db_table_comment = 'Categoria dos tickets do sistema.'
        indexes = [
            models.Index(fields=["name"], name="category_name_idx"),
        ]
        unique_together = ["name"]