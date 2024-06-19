# Generated by Django 5.0.6 on 2024-06-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoz', '0002_priority_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name_plural': 'Priority'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(default='High', max_length=10, verbose_name='Priority'),
        ),
    ]