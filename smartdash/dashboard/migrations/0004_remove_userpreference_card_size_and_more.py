# Generated by Django 5.2.4 on 2025-07-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_userpreference_card_size_userpreference_layout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreference',
            name='card_size',
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='layout',
        ),
    ]
