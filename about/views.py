from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutMe

class AboutMeView(TemplateView):
    template_name = 'about/aboutme.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data()
        context['about'] = AboutMe.objects.first()
        return context
