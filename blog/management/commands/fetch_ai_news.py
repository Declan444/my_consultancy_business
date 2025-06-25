from django.core.management.base import BaseCommand
from blog.models import NewsArticle
import feedparser
import os
from openai import OpenAI
from django.utils import timezone
from datetime import datetime
import time


class Command(BaseCommand):
    help = "Fetch latest AI business news, summarize with OpenAI, and store in NewsArticle."

    FEEDS = [
        "https://hbr.org/rss/topic/artificial-intelligence",
        "https://venturebeat.com/category/ai/feed/",
        "https://www.technologyreview.com/feed/",
    ]

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Fetching AI news feeds..."))
        all_entries = []
        for url in self.FEEDS:
            feed = feedparser.parse(url)
            for entry in feed.get("entries", []):
                all_entries.append(
                    {
                        "title": entry.get("title", "No title"),
                        "link": entry.get("link", "#"),
                        "published": entry.get("published_parsed"),
                        "source": url,
                    }
                )
        # Sort by published date, most recent first
        all_entries = [e for e in all_entries if e["published"]]
        all_entries.sort(key=lambda e: e["published"], reverse=True)
        articles = all_entries[:5]
        # Convert published to datetime
        for a in articles:
            a["published"] = datetime.fromtimestamp(
                time.mktime(a["published"]), tz=timezone.utc
            )
        # Prepare summary prompt
        headlines = [a["title"] for a in articles]
        prompt = (
            "Summarize the following AI business news headlines in a few sentences. "
            "Highlight 2-3 key trends or insights for business owners:\n\n"
            + "\n".join(f"- {title}" for title in headlines)
        )
        api_key = os.environ.get("OPENAI_API_KEY")
        summary = ""
        if api_key:
            try:
                client = OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=400,
                    temperature=0.7,
                )
                summary = response.choices[0].message.content
            except Exception as e:
                summary = f"Error generating summary: {e}"
        else:
            summary = "OpenAI API key not set."
        # Store articles and summary in DB, avoid duplicates
        for a in articles:
            obj, created = NewsArticle.objects.get_or_create(
                title=a["title"],
                link=a["link"],
                defaults={
                    "published": a["published"],
                    "summary": summary,
                    "source": a["source"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {a['title']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {a['title']}"))
        self.stdout.write(self.style.SUCCESS("Done."))
