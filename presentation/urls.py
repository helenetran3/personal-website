from django.urls import path

from . import views

app_name = 'presentation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact_submitted/', views.SubmittedView.as_view(), name='submitted'),
    path('contact/submit/', views.get_form, name='submit_form'),
]
