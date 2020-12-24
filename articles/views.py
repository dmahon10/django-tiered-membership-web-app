from itertools import chain

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.db.models import Q
from django.views.generic import DetailView, ListView

from .models import Article, FreeArticle, PremiumArticle


class FreeArticleListView(ListView): 
    model = FreeArticle
    context_object_name = 'article_list'
    template_name = 'articles/articles_list.html'

class FreeArticleDetailView(DetailView):
    model = FreeArticle
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

class PremiumArticleListView(ListView):
    model = PremiumArticle
    context_object_name = 'article_list'
    template_name = 'articles/articles_list.html'
    login_url = 'account_login'
    permission_required = 'articles.premium_member'

class PremiumArticleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PremiumArticle
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'
    login_url = 'account_login'
    permission_required = 'articles.premium_member'
    
class SearchResultsListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articles/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        free = FreeArticle.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        premium = PremiumArticle.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return chain(free, premium)
        
