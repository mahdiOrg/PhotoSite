from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='کاربر')
    info = models.TextField(max_length=700, verbose_name='اطلاعات')
    image = models.ImageField(upload_to='profile/', blank=True, null=True, verbose_name='تصویر')

    class Meta:
        verbose_name = "پروفایل "
        verbose_name_plural = "پروفایل ها"

    def __str__(self):
        return self.user.username
