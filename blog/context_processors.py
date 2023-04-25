from . import models

def new_articles(request):
    categories = models.BlogCategory.objects.all()
    new_articles = models.Article.objects.all()[:4]

    return {
        'new_articles':new_articles,
        'categories':categories
    }