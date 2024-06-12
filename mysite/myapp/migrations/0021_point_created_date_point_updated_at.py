# Generated by Django 5.0.6 on 2024-06-12 10:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_point_operator_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]