# Generated by Django 4.1.2 on 2022-10-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image_path',
            field=models.CharField(max_length=256, null=True, verbose_name='Image_path'),
        ),
    ]
