from django.contrib import admin
from curdapp.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('id', 'cname', 'cemail', 'caddrs', 'cphone', 'cincome')
    list_display_links = ('id', 'cname')

admin.site.register(Company, CompanyAdmin)
