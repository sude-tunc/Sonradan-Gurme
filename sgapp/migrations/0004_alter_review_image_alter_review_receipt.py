# Generated by Django 5.1.6 on 2025-05-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sgapp", "0003_review_image_review_receipt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="review_images/"),
        ),
        migrations.AlterField(
            model_name="review",
            name="receipt",
            field=models.ImageField(
                blank=True, null=True, upload_to="review_receipts/"
            ),
        ),
    ]
