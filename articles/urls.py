from django.urls import path

from .views import (FreeArticleDetailView, FreeArticleListView,
                    PremiumArticleDetailView, PremiumArticleListView,
                    SearchResultsListView)

urlpatterns = [
    path('free/', FreeArticleListView.as_view(), name='free_article_list'),
    path('premium/', PremiumArticleListView.as_view(), name='premium_article_list'),
    path('free/<slug:slug>', FreeArticleDetailView.as_view(), name='free_article_detail'),
    path('premium/<slug:slug>', PremiumArticleDetailView.as_view(), name='premium_article_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]

