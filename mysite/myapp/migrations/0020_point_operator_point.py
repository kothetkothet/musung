# Generated by Django 5.0.6 on 2024-06-12 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_licencedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='operator',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.point'),
        ),
    ]
