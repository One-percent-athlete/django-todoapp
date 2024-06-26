# Generated by Django 5.0.6 on 2024-06-19 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'priority',
            },
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todoz.priority'),
        ),
    ]
