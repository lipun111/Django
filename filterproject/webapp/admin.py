from django.contrib import admin
from webapp.models import Filter
# Register your models here.


class FilterAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'dept', 'date']

admin.site.register(Filter, FilterAdmin)
