from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path('blog/', include('blog.urls', namespace='blog')),
    path('quiz/', include('quiz.urls')),
    path('aboutme/', include('aboutme.urls', namespace='aboutme')),
    path('businessconsulting/', include('business_consulting.urls', namespace='business_consulting')),
    path('digitalconsulting/', include('digital_consulting.urls', namespace='digital_consulting')),
    
    path("newsletter/", include("newsletter.urls")),
    path("summernote/", include("django_summernote.urls")),
    path('contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
