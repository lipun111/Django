from django.contrib import admin
from webapp.models import Beer
# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    list_display=['name', 'test', 'color','price']


admin.site.register(Beer, BeerAdmin)
