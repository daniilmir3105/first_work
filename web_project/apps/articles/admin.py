from django.contrib import admin
# from models import Article, Comment
from . import models

Article = models.Article
Comment = models.Comment

# регистрируем наши модели в админку
admin.site.register(Article)
admin.site.register(Comment)
