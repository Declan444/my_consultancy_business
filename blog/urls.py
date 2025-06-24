from django.urls import path
from . import views
from .views import latest_ai_news

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path(
        "blog/<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path("<int:post_id>/share/", views.post_share, name="post_share"),
    path("latest-ai-news/", latest_ai_news, name="latest_ai_news"),
]
