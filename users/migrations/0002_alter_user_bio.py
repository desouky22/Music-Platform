# Generated by Django 4.1.3 on 2022-11-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(max_length=256, null=True),
        ),
    ]