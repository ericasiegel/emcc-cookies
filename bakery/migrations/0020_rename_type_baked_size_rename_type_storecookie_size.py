# Generated by Django 4.1.5 on 2023-01-30 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bakery", "0019_cookie_mini_cookie_par"),
    ]

    operations = [
        migrations.RenameField(
            model_name="baked",
            old_name="type",
            new_name="size",
        ),
        migrations.RenameField(
            model_name="storecookie",
            old_name="type",
            new_name="size",
        ),
    ]
