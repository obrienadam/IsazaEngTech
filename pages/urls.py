from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ContactView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/index.html'), name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    url(r'^services/$', TemplateView.as_view(template_name='pages/services.html'), name='services'),
    url(r'^services/advanced-mathematical-modelling/$',
        TemplateView.as_view(template_name='pages/advanced_mathematical_modelling.html'),
        name='services-advanced-mathematical-modelling'),
    url(r'^services/custom-engineering-software/$',
        TemplateView.as_view(template_name='pages/custom_engineering_software.html'),
        name='services-custom-engineering-software'),
    url(r'^careers/$', TemplateView.as_view(template_name='pages/careers.html'), name='careers'),
    url(r'^contact/$', ContactView.as_view(), name='contact')
]
