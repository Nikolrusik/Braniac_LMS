from django.contrib import admin
from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(mainapp_models.Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'teacher', 'deleted']
# Register your models here.
