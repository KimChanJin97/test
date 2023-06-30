from django.contrib import admin

from field.models import Field


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'field')
    # list_filter = ('',)
