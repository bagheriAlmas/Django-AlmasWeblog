import site

from django.contrib import admin

from articles.models import Article, Category, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    fields = ['owner', 'article', 'content']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'author', 'slug')}),
        ('Content', {'fields': ('description', 'content', 'image', 'resource')}),
        ('Content Info', {'fields': ('read_time', 'status', 'categories')}),
        ('Important Dates', {'fields': ('created', 'updated')}),
    )

    readonly_fields = ['slug', 'created', 'updated']
    list_display = ['id', 'title', 'author', 'status', 'created', 'updated']
    list_filter = ['author__username', 'status']
    search_fields = ['author__username', 'title']
    filter_horizontal = ['categories']
    inlines = [CommentInline, ]

    # Each User Can Manage own Articles
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


admin.site.register(Category)
