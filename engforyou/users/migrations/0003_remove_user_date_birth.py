# Generated by Django 5.1.2 on 2025-04-20 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_birth',
        ),
    ]
