from django.contrib import admin
from webapp.models import Gpl
# Register your models here.


class GplAdmin(admin.ModelAdmin):
    list_display = ['team', 'owner', 'phoneno', 'captain', 'icon', 'golden']


admin.site.register(Gpl, GplAdmin)