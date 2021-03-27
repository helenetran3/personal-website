from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'presentation/index.html'


class EducationView(generic.TemplateView):
    template_name = 'presentation/education.html'


class ProjectsView(generic.TemplateView):
    template_name = 'presentation/projects.html'


class ContactView(generic.TemplateView):
    template_name = 'presentation/contact.html'
