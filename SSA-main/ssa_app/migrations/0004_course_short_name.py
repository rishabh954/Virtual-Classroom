# Generated by Django 5.0 on 2024-03-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssa_app', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='short_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
