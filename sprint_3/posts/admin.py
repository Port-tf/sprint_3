from django.contrib import admin

from .models import Author, Biografy, Poem 


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'pub_date', 'user')
    search_fields = ('text',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'name_url', 'description')


class BiografyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'birthday', 'date_of_death', 'text')

 
admin.site.register(Poem, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Biografy, BiografyAdmin)
