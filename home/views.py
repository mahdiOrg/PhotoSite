from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from projects import models


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_projects'] = models.Project.objects.all()[:9]
        best_projects = models.Project.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:6] # ordering projects by likes number
        context['best_projects'] = best_projects
        return context
