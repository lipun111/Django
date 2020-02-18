from django.contrib import admin
from webapp.models import Emp


class EmpAdmin(admin.ModelAdmin):
    list_display = ['name', 'eid', 'salary']
# Register your models here.


admin.site.register(Emp, EmpAdmin)