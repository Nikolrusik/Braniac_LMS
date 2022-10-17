from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import get_object_or_404


from mainapp.models import News, Courses
# Create your views here.


class IndexPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)

        context['news'] = News.objects.all()
        context['range'] = range(5)
        return context


class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(News, pk=pk)
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesPageView, self).get_context_data(**kwargs)
        context["objects"] = Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(
            Courses, pk=pk
        )
        context["lessons"] = Lesson.objects.filter(
            course=context["course_object"]
        )
        context["teachers"] = CourseTeachers.objects.filter(
            course=context["course_object"]
        )
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocumentosPageView(TemplateView):
    template_name = "mainapp/doc_site.html"
