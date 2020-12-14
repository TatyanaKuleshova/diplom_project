from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.tag_name}'

class Article(models.Model):
    article_name = models.CharField(max_length = 100)
    article_text = models.CharField(max_length = 10000)
    article_data = models.DateTimeField('Дата публикации:')
    article_tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.article_name}, опубликовано: {self.article_data}'

