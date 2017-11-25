from django import forms
from django.core import mail


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your e-mail'
    }))

    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a subject'
    }))

    message = forms.CharField(required=True, max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter a message'
    }))

    attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))

    def send_email(self):
        msg = mail.EmailMessage(
            subject=self.cleaned_data['subject'],
            body=self.cleaned_data['message'],
            to=['pedro.isaza@isazaengtech.com', 'a.obrien@mail.utoronto.ca'],
            reply_to=[self.cleaned_data['email']]
        )

        msg.send()
