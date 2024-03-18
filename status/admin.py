from django.contrib import admin
from.models import Status


@admin.register(Status)
class StatusModelAdmin(admin.ModelAdmin):
    model = Status
    list_display = ("name", "created_at", "updated_at", "is_active")
    fieldsets = (
            (None, {
                'fields': (
                    'name',
                )
            }),
            ('Informações', {
                'fields': (
                      "is_active",
                )
            }),
            ('Datas Importantes', {
                'fields': (
                    "created_at", "updated_at",
                )
            }),
        )
    search_fields = ('name', 'created_at', 'is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at', )