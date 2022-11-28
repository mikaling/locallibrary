from django.contrib import admin
from .models import  Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


# BookInline for Author detail view
class BooksInline(admin.StackedInline):
    model = Book
    extra = 0

# define the (author) admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = [
        'first_name', 
        'last_name', 
        # tuple displays fields horizontally
        ('date_of_birth', 'date_of_death')
        ]
    
    inlines = [BooksInline]

# register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# BookInstanceInline
class BooksInstanceInline(admin.TabularInline):
        model = BookInstance
        extra = 0 # no extra rows in BookInstancesInline table


# register admin class for Book using the @register decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    # display related BookInstances in detail view
    inlines = [BooksInstanceInline]
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    # fieldsets for sectioning the detail view form
    fieldsets = (
        (None, {
            "fields": ('book', 'imprint', 'id'),
        }),
        ('Availability', {
            "fields": ('status', 'due_back')
        }),
    )
    

