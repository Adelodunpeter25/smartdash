# Generated by Django 5.2.4 on 2025-07-15 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_userpreference_card_size_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPreference',
        ),
    ]
