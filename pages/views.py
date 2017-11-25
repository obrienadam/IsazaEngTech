# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import FormView

from forms import ContactForm

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)