from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('booksoft.urls')),
    path('', include('workflow.urls')),
    path('', include('post.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^blog/comments/', include('fluent_comments.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

