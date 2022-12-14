# Generated by Django 4.1.1 on 2022-10-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='As markdown')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creating')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of editing')),
            ],
        ),
    ]
