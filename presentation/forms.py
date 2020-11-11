from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(initial="Sujet",max_length=100)
    message = forms.CharField(initial="Mon Message",widget=forms.Textarea)
    sender = forms.EmailField(initial="a@a.com")
