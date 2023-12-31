# Generated by Django 4.2.3 on 2023-07-08 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0002_book_thumbnail_alter_book_author_alter_book_isbn_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="book",
            name="thumbnail",
            field=models.URLField(),
        ),
    ]
