from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Local
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('payments/', include('payments.urls')), 

    # Third party
    path('accounts/', include('allauth.urls')), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
