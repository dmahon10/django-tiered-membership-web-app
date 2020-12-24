from django.contrib import admin

from .models import Comment, FreeArticle, PremiumArticle


class CommentInline(admin.TabularInline): 
    model = Comment

class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        CommentInline,
    ]
    list_display = ("title", "author")

admin.site.register(FreeArticle, ArticleAdmin)
admin.site.register(PremiumArticle, ArticleAdmin)

