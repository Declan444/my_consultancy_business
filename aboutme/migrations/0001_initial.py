# Generated by Django 4.2.18 on 2025-02-03 20:42

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutMe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title for the About Me page", max_length=200
                    ),
                ),
                (
                    "content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True,
                        help_text="Main content for the About Me page (will be used as overview)",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Optional image for the About Me page",
                        null=True,
                        upload_to="aboutme/",
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "overview",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Overview text displayed next to image"
                    ),
                ),
                (
                    "section1_title",
                    models.CharField(
                        default="Section 1",
                        help_text="Title for first section",
                        max_length=200,
                    ),
                ),
                (
                    "section1_content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Content for first section"
                    ),
                ),
                (
                    "section2_title",
                    models.CharField(
                        default="Section 2",
                        help_text="Title for second section",
                        max_length=200,
                    ),
                ),
                (
                    "section2_content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Content for second section"
                    ),
                ),
                (
                    "section3_title",
                    models.CharField(
                        default="Section 3",
                        help_text="Title for third section",
                        max_length=200,
                    ),
                ),
                (
                    "section3_content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Content for third section"
                    ),
                ),
                (
                    "section4_title",
                    models.CharField(
                        default="Section 4",
                        help_text="Title for fourth section",
                        max_length=200,
                    ),
                ),
                (
                    "section4_content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Content for fourth section"
                    ),
                ),
                (
                    "section5_title",
                    models.CharField(
                        default="Section 5",
                        help_text="Title for fifth section",
                        max_length=200,
                    ),
                ),
                (
                    "section5_content",
                    django_summernote.fields.SummernoteTextField(
                        blank=True, help_text="Content for fifth section"
                    ),
                ),
            ],
        ),
    ]
