from django.contrib import admin
from webapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display =['name','marks']
# Register your models here.

admin.site.register(Student, StudentAdmin)
