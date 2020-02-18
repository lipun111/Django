from django.contrib import admin
from webapp.models import *
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ['Eid', 'Ename', 'Esal', 'Eaddr']


admin.site.register(Emp, EmpAdmin)


class StuAdmin(admin.ModelAdmin):
    list_display = ['Sid', 'Sname', 'Ssal', 'Saddr']


admin.site.register(Stu, StuAdmin)
