from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="main_page"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),

    path("courses/", views.CoursesPageView.as_view(), name="courses"),
    path(
        "courses/<int:pk>/",
        views.CoursesDetailView.as_view(),
        name="courses_detail",
    ),
    path("documentos/", views.DocumentosPageView.as_view(), name="documentos"),
]
