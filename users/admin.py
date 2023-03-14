from django.contrib import admin

from users.models import CustomUser


# Register your models here.

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User Info', {'fields': ('first_name', 'last_name', 'username', 'password')}),
        ('Socials', {'fields': ('email', 'facebook', 'twitter')}),
        ('About User', {'fields': ('avatar', 'about_me')}),
        ('Important Settings', {'fields': ('is_staff','is_active','is_superuser')}),
    )

    list_display = ['id', 'first_name', 'last_name', 'username','email', 'is_staff']
    # list_filter = ['author__username', 'status']
    # search_fields = ['author__username', 'title']
    # filter_horizontal = ['categories']
