from django.contrib import admin
from . import models
from projects_media.models import Image, Video


class ImageInline(admin.TabularInline):
    model = Image


class VideoInline(admin.TabularInline):
    model = Video


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        VideoInline,
    ]


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Category)
admin.site.register(models.Like)
