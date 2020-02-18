from django.contrib import admin
from webapp.models import Emp
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ['Eid', 'Ename','Esal', 'Eaddr']


admin.site.register(Emp, EmpAdmin)