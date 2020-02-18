from django.contrib import admin
from webapp.models import Emplyoee
# Register your models here.

class EmplyoeeAdmin(admin.ModelAdmin):
    list_display=('id','ename', 'eid', 'esal', 'eaddrs')
    list_display_links=('id', 'ename')

admin.site.register(Emplyoee, EmplyoeeAdmin)
