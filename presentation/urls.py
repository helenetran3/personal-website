from django.urls import path

from . import views

app_name = 'presentation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
