# Generated by Django 4.1.1 on 2022-10-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_courses_teachers_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
