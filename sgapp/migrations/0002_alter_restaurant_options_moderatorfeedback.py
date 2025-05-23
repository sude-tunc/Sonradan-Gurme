# Generated by Django 5.1.6 on 2025-05-15 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("sgapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="restaurant",
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="ModeratorFeedback",
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
                ("object_id", models.PositiveIntegerField()),
                (
                    "decision",
                    models.CharField(
                        choices=[("approved", "Onaylandı"), ("rejected", "Reddedildi")],
                        max_length=20,
                    ),
                ),
                ("feedback_text", models.TextField(blank=True)),
                ("is_read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
