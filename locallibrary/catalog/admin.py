from django.contrib import admin

# Register your models here.

from catalog.models import Author, Language, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class BooksInline(admin.TabularInline):
    model = Book
    fields = ('isbn', 'title')
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
    pass

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    fields = ('id', 'imprint', 'due_back', 'status')
    extra = 0
    readonly_fields = ('id',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    
    list_filter = ('status', 'due_back')

    fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'id')
                }),
            ('Availability', {
                'fields': ('status', 'due_back')
                }),
    )
    pass
