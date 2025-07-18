from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Post, NewsArticle
from django.http import Http404
from .forms import EmailPostForm
from openai import OpenAI
import feedparser
import os
from django.views.decorators.cache import cache_page


def post_list(request):
    post_list = Post.published.all()

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})


def post_share(request, post_id):
    #
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    recipient_email = None
    if request.method == "POST":
        # form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form is valid
            cd = form.cleaned_data
            # send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = (
                f"{cd['name']} ({cd['email']}) recommends you read " f"{post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd["to"]],
            )

            sent = True
            recipient_email = cd["to"]

    else:
        form = EmailPostForm()
    return render(
        request,
        "blog/post/share.html",
        {"post": post, "form": form, "sent": sent, "recipient_email": recipient_email},
    )


@cache_page(60 * 30)  # Cache for 30 minutes
def latest_ai_news(request):
    # Read the 5 most recent news articles from the database
    articles = NewsArticle.objects.order_by("-published")[:5]
    headlines = [(a.title, a.link) for a in articles]
    summary = articles[0].summary if articles else "No summary available."
    return render(
        request,
        "blog/latest_ai_news.html",
        {
            "headlines": zip([a.title for a in articles], [a.link for a in articles]),
            "summary": summary,
        },
    )
