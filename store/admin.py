from django.contrib import admin
from .models import Author, Book, PublishedBook, EBook

# Admin site branding
admin.site.site_header = "BookStore Admin"
admin.site.site_title = "BookStore Admin Portal"
admin.site.index_title = "Welcome to BookStore Admin Panel"

# Inline book form within author admin
class BookInline(admin.TabularInline):
    model = Book
    extra = 1

# Author admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    inlines = [BookInline]

# Book admin (regular books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('published_date',)
    ordering = ('-published_date',)
    readonly_fields = ('id',)

# Proxy model admin (PublishedBook)
class PublishedBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'published']

# Multi-table model admin (EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'file_format', 'download_url']

# Registering all models
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(PublishedBook, PublishedBookAdmin)
admin.site.register(EBook, EBookAdmin)