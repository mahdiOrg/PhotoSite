from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    info = models.TextField(verbose_name="توضیحات")
    photographer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='projects', null=True,
                                     verbose_name="عکاس")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='projects', null=True,
                                 verbose_name="دسته بندی")
    location = models.CharField(max_length=500, null=True, blank=True, verbose_name="مکان")
    customer = models.CharField(max_length=500, null=True, blank=True, verbose_name="مشتری")
    date = models.DateField(blank=True, null=True, verbose_name="تاریخ")
    add_time = models.DateField(auto_now_add=True)

    def num_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ('-add_time',)
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه ها'

    def get_absolute_url(self):
        return reverse('projects:projects_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

    def __str__(self):
        return self.user.username + self.project.title


