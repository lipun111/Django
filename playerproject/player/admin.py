from django.contrib import admin
from player.models import Player
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'grade', 'price','phoneno']

admin.site.register(Player, PlayerAdmin)
