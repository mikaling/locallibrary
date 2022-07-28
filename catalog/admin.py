from django.contrib import admin
from .models import  Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# register admin class for Book usint the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

