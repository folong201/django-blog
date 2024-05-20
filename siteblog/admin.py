from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.CustomUser) 
admin.site.register(models.Article)
admin.site.register(models.Publication)
admin.site.register(models.Like)
admin.site.register(models.Comment)

