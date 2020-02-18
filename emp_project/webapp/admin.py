from django.contrib import admin
from webapp.models import Signup


class SignupAdmin(admin.ModelAdmin):
    list_display = ['name', 'phoneno', 'city', 'email']
# Register your models here.


admin.site.register(Signup, SignupAdmin)