# Generated by Django 2.2.7 on 2020-01-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0007_auto_20200107_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
