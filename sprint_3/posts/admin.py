from django.contrib import admin

from .models import Author, Poem 


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'pub_date', 'user')
    search_fields = ('text',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'name_url', 'description')

 
admin.site.register(Poem, PostAdmin)
admin.site.register(Author, AuthorAdmin)