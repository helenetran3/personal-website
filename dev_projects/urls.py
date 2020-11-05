from django.urls import path

from . import views

app_name = 'dev_projects'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
