# Generated by Django 2.2.7 on 2020-01-07 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0005_auto_20200107_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='category',
            new_name='course',
        ),
    ]
