from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Category, Like
from projects_media.models import Image, Video


class ProjectsListView(ListView):
    model = Project
    context_object_name = 'projects'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.GET.get('category')
        if category_title is not None:
            if category_title == 'bests':
                queryset = queryset.annotate(num_likes=Count('likes')).order_by('-num_likes')
            else:
                category = get_object_or_404(Category, title=category_title)
                queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data()
        context['projects_pics'] = self.object.images.all()
        context['project_videos'] = self.object.videos.all()
        if self.request.user.is_authenticated:
            if self.request.user.likes.filter(project_id=self.object.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False

        return context


def like(request, project_id):
    try:
        like_object = Like.objects.get(project_id=project_id, user_id=request.user.id)
        like_object.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(project_id=project_id, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})
