# Generated by Django 2.2.7 on 2020-01-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0006_auto_20200107_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='../media/files'),
        ),
    ]
