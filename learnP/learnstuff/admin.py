from django.contrib import admin
from .models import Book_stem, Author, Address

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ("author", "rating")

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book_stem, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)