from django.db import models
import datetime
from django.utils import timezone
# from abc import ABCMeta
# здесь мы создаем модели того, что будет в приложении
# конкретные элементы мы задаем полями в классах

class Article(models.Model):
    # поле для ввода небольшого текста (max_length - обязателен)
    article_title = models.CharField('Title of article', max_length=100)
    # поле для ввода большого текста(max_length = 20000 ~ 30000,
    # необязательный параметр )
    article_text = models.TextField('Text of article')
    public_date = models.DateTimeField('Date of publication')  # поле для даты

    def __str__(self):  # лучше всегда прописывать
        return self.article_title

    def was_published_recently(self):
        return self.public_date >= (timezone.now() - datetime.timedelta(days=7))

    # перевод на русский язык наших разделов в админке
    class Meta:
        verbose_name = 'Статья'  # in singular-form
        verbose_name_plural = 'Статьи'  # in plural-form


class Comment(models.Model):
    # внешний ключ - прикрепляющий модель(комментарий) к модели(статье)
    # при удалении применяется каскад
    # (когда удаляется статья будут удалены и все комментарии к ней)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField('Name of autor', max_length=50)
    comment_text = models.CharField('Text of comment', max_length=200)

    def __str__(self):
        return self.autor_name

    class Meta:
        verbose_name = 'Комментарий'  # in singular-form
        verbose_name_plural = 'Комментарии'  # in plural-form
