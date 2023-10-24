from django.contrib import admin
from .models import Author, Article, Commentary


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'email')
    ordering = ('surname', 'name',)
    list_filter = ('name',)
    search_fields = ('name', )
    readonly_fields = ['birthday']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'surname', ],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse'],
                'fields': ['email']
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'fields': ['biography', 'birthday'],
            }
        ),
    ]


class CommentaryAdmin(admin.ModelAdmin):

    list_display = ('author', 'article', 'publication_date', )
    ordering = ('publication_date', )
    list_filter = ('author', 'article', 'publication_date', )
    search_fields = ('content', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(Article)
