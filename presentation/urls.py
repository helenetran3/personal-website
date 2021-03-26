from django.urls import path

from . import views

app_name = 'presentation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
