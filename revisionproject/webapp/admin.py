from django.contrib import admin
from webapp.models import Revision
# Register your models here.

class RevisionAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'phone', 'email', 'addrs')
    list_display_links = ('name', 'phone')


admin.site.register(Revision, RevisionAdmin)
