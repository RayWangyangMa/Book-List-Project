# Generated by Django 4.2.3 on 2023-07-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="thumbnail",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name="book",
            name="pub_date",
            field=models.CharField(max_length=200),
        ),
    ]
