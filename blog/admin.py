from django.contrib import admin
from .models import Post

# Register your models here.


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]


admin.site.register(Post, PostAdmin)
