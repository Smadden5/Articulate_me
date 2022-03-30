from django.contrib import admin

from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title", "author"]

    list_filter = ["created_date"]

    prepopulated_fields = {'slug':('title',)} 

    class Meta:
        model = Article

class CommentAdmin(admin.ModelAdmin):

    list_display = ["comment_author","comment_content","created_date"]
    list_display_links = ["comment_author","comment_content","created_date"]
    search_fields = ["comment_author","created_date"]
    list_filter = ["created_date"]
    
    class Meta:
        model = Article

