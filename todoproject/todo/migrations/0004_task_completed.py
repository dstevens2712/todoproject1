# Generated by Django 4.0.4 on 2022-04-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
