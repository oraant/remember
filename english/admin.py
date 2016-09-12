from django.contrib import admin
from english.models import Book, Word, Group

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'words']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'name', 'desc', 'words']

class WordAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'name', 'desc']

admin.site.register(Book, BookAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Word, WordAdmin)