from django.contrib import admin
from django.contrib.auth.models import User
from . import models


class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.BlogCategory)
admin.site.register(models.Comment)
