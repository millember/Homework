# Generated by Django 4.2 on 2024-09-24 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0006_alter_version_is_actual"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Введите владельца товара",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
