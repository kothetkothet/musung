# Generated by Django 5.0.6 on 2024-06-05 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_workinghour'),
    ]

    operations = [
        migrations.CreateModel(
            name='operatortargetrep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optarget', models.PositiveIntegerField(default=0)),
                ('totalqty', models.PositiveIntegerField(default=0)),
                ('percent', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.line')),
                ('operatorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.operator')),
            ],
        ),
        migrations.CreateModel(
            name='hourlytargetrep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrqty', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('timehr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.workinghour')),
                ('optname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.operatortargetrep')),
            ],
        ),
    ]
