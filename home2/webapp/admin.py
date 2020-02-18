from django.contrib import admin
from webapp.models import Gpl

# Register your models here.


class GplAdmin(admin.ModelAdmin):
    list_display = ['teamname', 'match', 'win', 'lose', 'draw', 'point']


admin.site.register(Gpl, GplAdmin)