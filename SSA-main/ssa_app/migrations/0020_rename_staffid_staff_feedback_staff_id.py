# Generated by Django 5.0 on 2024-03-27 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssa_app', '0019_rename_staff_id_staff_feedback_staffid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_feedback',
            old_name='staffid',
            new_name='staff_id',
        ),
    ]
