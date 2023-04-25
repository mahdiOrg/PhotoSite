from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BlogCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    author = models.ForeignKey(User, related_name='articles', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name="نویسنده")
    content = models.TextField(verbose_name='محتوا')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, related_name='articles', null=True,
                                 verbose_name='دسته بندی')
    image1 = models.ImageField(upload_to='article/image', verbose_name='عکس 1')
    image2 = models.ImageField(upload_to='article/image', blank=True, null=True, verbose_name='عکس2')
    image3 = models.ImageField(upload_to='article/image', blank=True, null=True, verbose_name='عکس3')
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-add_time',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments', verbose_name="کاربر")
    content = models.TextField(max_length=400, verbose_name="متن کامنت")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_comments', blank=True, null=True)
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return self.article.title +self.content[:30]
