from django.contrib import admin
from curdapp.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','name','ceo','addrs', 'email')
    list_display_links=('id','name')

admin.site.register(Company, CompanyAdmin)
