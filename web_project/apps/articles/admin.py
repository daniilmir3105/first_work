from django.contrib import admin
# from models import Article, Comment
from . import models

Article = models.Article
Comment = models.Comment

# регистрируем наши модели в админку, чтобы они там появились 
admin.site.register(Article)
admin.site.register(Comment)
