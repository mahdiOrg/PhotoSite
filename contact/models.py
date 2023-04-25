from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message', verbose_name='کاربر')
    content = models.TextField(verbose_name='پیام')
    email = models.EmailField(blank=True, null=True)
    add_time = models.DateField(auto_now_add=True, )
    checked = models.BooleanField(default=False, verbose_name='خوانده شده')

    class Meta:
        ordering = ('checked',)
        verbose_name = 'پیغام'
        verbose_name_plural = 'پیغام ها'

    def __str__(self):
        return self.user.username + self.content[:40]


class ContactWay(models.Model):
    contactInfo = models.TextField(blank=True, null=True, verbose_name='توضیحات راه های ارتباطی')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    phone = models.DecimalField(decimal_places=0,max_digits=12, blank=True, null=True, verbose_name='شماره تماس')
    email = models.EmailField(blank=True, null=True,verbose_name='ایمیل')

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

    def __str__(self):
        return self.contactInfo[:50]

