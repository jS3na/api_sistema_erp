# Generated by Django 4.2.4 on 2025-01-01 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_group_user_groups_group_permissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='admin',
            new_name='is_owner',
        ),
    ]
