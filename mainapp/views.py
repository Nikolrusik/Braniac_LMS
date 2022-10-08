from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "mainapp/index.html"


class News(TemplateView):
    template_name = "mainapp/news.html"


class Courses(TemplateView):
    template_name = "mainapp/courses_list.html"


class Contacts(TemplateView):
    template_name = "mainapp/contacts.html"


class Documentos(TemplateView):
    template_name = "mainapp/doc_site.html"


class Login(TemplateView):
    template_name = "mainapp/login.html"
