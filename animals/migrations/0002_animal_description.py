# Generated by Django 4.2.3 on 2023-07-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="description",
            field=models.TextField(default="Default description", max_length=100),
        ),
    ]
