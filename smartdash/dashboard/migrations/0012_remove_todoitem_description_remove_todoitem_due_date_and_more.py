# Generated by Django 5.2.4 on 2025-07-25 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_todoitem_description_todoitem_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='updated_at',
        ),
    ]
