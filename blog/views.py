from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from . import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm


class ArticleListView(ListView):
    model = models.Article
    template_name = 'blog/blog.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        context['new_aticles'] = models.Article.objects.all()[:4]
        context['categories'] = models.BlogCategory.objects.all()
        return context

    def get_queryset(self):
        query = super().get_queryset()
        search = self.request.GET.get('search')
        category_title = self.request.GET.get('category')
        if search is not None:
            query = query.filter(title__icontains=search)

        if category_title is not None:
            category = get_object_or_404(models.BlogCategory, title=category_title)
            query = query.filter(category=category)

        return query


class ArticleDetailView(DetailView):
    model = models.Article
    context_object_name = 'article'

    def post(self, *args,**kwargs):
        article = self.get_object()
        form = CommentForm(self.request.POST)

        if form.is_valid():
            form.save(article=article, author=self.request.user)
            return redirect('blog:article_detail', pk=article.pk)
        else:
            return redirect('blog:article_detail', pk=article.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
