from django.contrib import admin
from webapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['titile','auther','pages','price']


admin.site.register(Book, BookAdmin)
