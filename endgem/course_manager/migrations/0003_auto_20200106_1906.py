# Generated by Django 2.2.7 on 2020-01-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0002_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deptt',
            field=models.CharField(default='NIL', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(default='DEFAULT', max_length=3, unique=True),
        ),
    ]
