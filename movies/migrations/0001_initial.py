# Generated by Django 4.1.7 on 2023-02-15 23:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=127)),
                ("duration", models.CharField(max_length=10, null=True)),
                (
                    "rating",
                    models.CharField(
                        choices=[
                            ("G", "Rated G"),
                            ("PG", "Rated Pg"),
                            ("PG-13", "Rated Pg 13"),
                            ("R", "Rated R"),
                            ("NC-17", "Rated Nc 17"),
                        ],
                        default="G",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("synopsis", models.TextField(null=True)),
            ],
        ),
    ]
