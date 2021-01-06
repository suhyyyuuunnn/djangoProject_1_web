from django.contrib import admin
from django.urls import path, include
from posts.views import intro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', intro),
    path('posts/', include('posts.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

