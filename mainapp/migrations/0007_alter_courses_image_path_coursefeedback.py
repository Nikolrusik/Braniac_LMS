# Generated by Django 4.1.2 on 2022-10-23 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0006_alter_courses_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image_path',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Image_path'),
        ),
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(default='No feedback', verbose_name='Feedback')),
                ('rating', models.SmallIntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], default=5, verbose_name='Rating')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('deleted', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.courses', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]