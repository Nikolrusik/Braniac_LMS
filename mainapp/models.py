from django.db import models
from mainapp.managers.news_manager import NewsManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Create your models here.


class News(models.Model):
    objects = NewsManager()

    title = models.CharField(
        max_length=256,
        verbose_name='Title'
    )
    preambule = models.CharField(
        max_length=1024,
        verbose_name='Preambule',
        blank=True,
        null=True
    )
    body = models.TextField(blank=False, null=False, verbose_name='Body')
    body_as_markdown = models.BooleanField(
        default=False,
        verbose_name='As markdown'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of editing',
        editable=False
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Courses(models.Model):
    objects = CoursesManager()

    title = models.CharField(
        max_length=256,
        verbose_name='Title'
    )
    image_path = models.CharField(
        max_length=256,
        verbose_name='Image_path',
        null=True,
        blank=True
    )
    body = models.TextField(verbose_name='Body')
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=8,
        decimal_places=2
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()


class Teachers(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=256
    )
    birthday = models.DateField(
        verbose_name='Birthday',
        editable=True
    )
    course = models.ForeignKey(
        'Courses',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    # Преподаватель может не вести никакой курс

    def __str__(self):
        return self.name

    def delete(self, *args):
        self.deleted = True
        self.save()


class Lessons(models.Model):
    title = models.CharField(
        verbose_name='Title',
        max_length=256
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creating',
        editable=False
    )
    lesson_date = models.DateTimeField(
        auto_now_add=False,
        verbose_name='Lesson date',
        editable=True,
        null=True,
        blank=True
    )
    teacher = models.ForeignKey(
        'Teachers',
        null=True,
        # Мы ведь можем иметь урок, на который ещё не назначен преподаватель
        on_delete=models.SET_NULL
    )

    course = models.ForeignKey('Courses', on_delete=models.CASCADE)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args):
        self.deleted = True
        self.save()


class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"), (1, "⭐"))
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, verbose_name=_("Course"))
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    feedback = models.TextField(
        default=_("No feedback"), verbose_name=_("Feedback"))
    rating = models.SmallIntegerField(
        choices=RATING, default=5, verbose_name=_("Rating"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course} ({self.user})"
