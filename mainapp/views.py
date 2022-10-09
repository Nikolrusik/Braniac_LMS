from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "mainapp/index.html"


class News(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        context['news_title'] = "Громкий новостной заголовок"
        context[
            'news_preview'
        ] = "Предварительное описание, которое заинтересует каждого"
        return context


class Courses(TemplateView):
    template_name = "mainapp/courses_list.html"


class Contacts(TemplateView):
    template_name = "mainapp/contacts.html"


class Documentos(TemplateView):
    template_name = "mainapp/doc_site.html"


class Login(TemplateView):
    template_name = "mainapp/login.html"
