# Generated by Django 5.0 on 2024-03-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssa_app', '0013_staff_notification_short_notification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
