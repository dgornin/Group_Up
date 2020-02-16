# Generated by Django 3.0.3 on 2020-02-14 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('groupsapp', '0002_group_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('3ab7bf08-2520-4b0a-8cf6-2e95c00dcfad'), verbose_name='uuid'),
        ),
    ]