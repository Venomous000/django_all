# Generated by Django 5.2.1 on 2025-06-03 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EBook",
            fields=[
                (
                    "book_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.book",
                    ),
                ),
                ("file_format", models.CharField(max_length=20)),
                ("download_url", models.URLField()),
            ],
            options={
                "abstract": False,
            },
            bases=("store.book",),
        ),
        migrations.CreateModel(
            name="PublishedBook",
            fields=[],
            options={
                "ordering": ["-created_at"],
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("store.book",),
        ),
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="book",
            name="updated_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="book",
            name="published_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
