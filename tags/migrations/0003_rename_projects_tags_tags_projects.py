# Generated by Django 4.2.1 on 2023-05-23 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tags_projects_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='projects_tags',
            new_name='projects',
        ),
    ]
