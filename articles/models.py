from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT_LEN = 1000


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # дата публикации
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/articles/%i/" % self.id

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text

