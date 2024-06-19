# Generated by Django 5.0.2 on 2024-06-18 20:44

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50, verbose_name='Task Name')),
                ('task_body', models.CharField(max_length=250, verbose_name='Task Body')),
                ('priority', models.CharField(default='normal', max_length=10, verbose_name='Priority')),
                ('deadline', models.DateTimeField(blank=True, verbose_name='Deadline')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todoz.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to='todoz.user')),
            ],
        ),
    ]
