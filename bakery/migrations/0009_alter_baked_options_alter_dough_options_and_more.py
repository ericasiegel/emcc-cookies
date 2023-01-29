# Generated by Django 4.1.5 on 2023-01-29 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bakery", "0008_alter_baked_options_alter_cookie_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="baked",
            options={"ordering": ["cookie"], "verbose_name": "Baked Cookie"},
        ),
        migrations.AlterModelOptions(
            name="dough",
            options={"ordering": ["cookie"], "verbose_name": "Cookie Dough"},
        ),
        migrations.AlterModelOptions(
            name="storecookie",
            options={"ordering": ["cookie"], "verbose_name": "Cookies In Store"},
        ),
        migrations.AlterField(
            model_name="storecookie",
            name="cookie",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="bakery.cookie"
            ),
        ),
    ]
