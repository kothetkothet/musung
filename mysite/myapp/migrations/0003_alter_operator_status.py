# Generated by Django 5.0.6 on 2024-06-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_line_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]