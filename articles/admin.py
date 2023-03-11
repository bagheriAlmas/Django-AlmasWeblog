import site

from django.contrib import admin

from articles.models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'author', 'slug')}),
        ('Content', {'fields': ('description','content', 'image')}),
        ('Content Info', {'fields': ('read_time','status','categories')}),
        ('Important Dates', {'fields': ('created', 'updated')}),
    )

    readonly_fields = ['slug']
    list_display = ['id', 'title', 'author', 'status', 'created', 'updated']
    list_filter = ['author__username', 'status']
    search_fields = ['author__username', 'title']
    filter_horizontal = ['categories']


admin.site.register(Category)