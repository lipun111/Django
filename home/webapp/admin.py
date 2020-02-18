from django.contrib import admin
from webapp.models import Player
# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phoneno', 'category', 'baseprice', 'bidprice', 'city']


admin.site.register(Player, PlayerAdmin)