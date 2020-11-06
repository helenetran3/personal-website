from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'presentation/index.html'


class ContactView(generic.TemplateView):
    template_name = 'presentation/contact.html'
