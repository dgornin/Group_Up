# Generated by Django 3.0.2 on 2020-01-27 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('groupsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('bb3af773-44e7-44cf-a787-2bc9f8e31825'), verbose_name='uuid'),
        ),
    ]