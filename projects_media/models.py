from django.db import models
from projects.models import Project


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name='پروژه')
    image = models.ImageField(upload_to='image/projects')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'

    def __str__(self):
        return self.project.title


class Video(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='videos', blank=True, null=True,
                                verbose_name='پروژه')
    video = models.FileField(upload_to='video/projects', help_text='حجم کمتر فیلم و فرمت mp4 به نمایش بهتر آن کمک میکند')

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'

    def __str__(self):
        return self.project.title
