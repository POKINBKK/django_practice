from django.contrib import admin
from social.models import Status, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'story', 'date', 'like', 'genre', 'writer']
    list_per_page = 10
    list_filter = ['genre']
    search_fields = ['topic']
    inlines = [CommentInline]


admin.site.register(Status, StatusAdmin)
