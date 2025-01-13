from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path('blog/', include('blog.urls', namespace='blog')),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('aboutme/', include('aboutme.urls', namespace='aboutme')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
