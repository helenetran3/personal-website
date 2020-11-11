from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'presentation/index.html'


class ContactView(generic.TemplateView):
    template_name = 'presentation/contact.html'


class SubmittedView(generic.TemplateView):
    template_name = 'presentation/submitted.html'


def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('presentation:submitted'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm(None)

    return render(request, 'presentation/contact.html', {'form': form})
