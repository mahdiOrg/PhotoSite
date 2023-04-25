from django.db import models


class AboutMe(models.Model):
    info = models.TextField(verbose_name='درباه من')
    image = models.ImageField(upload_to='image/about', verbose_name='عکس')
    add_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'

    def __str__(self):
        return self.info[:50]


class ContactInfo(models.Model):
    pass
