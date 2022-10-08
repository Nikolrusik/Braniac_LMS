from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.Index.as_view()),
    path("contacts/", views.Contacts.as_view()),
    path("news/", views.News.as_view()),
    path("login/", views.Login.as_view()),
    path("courses/", views.Courses.as_view()),
    path("documentos/", views.Documentos.as_view()),

]
