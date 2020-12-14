from django.core.management.base import BaseCommand
from articles.models import Tag, Article
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('DB command!') # проверили работу, все ли правильно


#выведем все статьи, которые есть на данный момент
        articles = Article.objects.all()
        print(articles)

# сделаем запрос на конкретную статью
        art_ = Article.objects.get(article_name = 'Адаптогены')
        print(art_)

# возвращает все теги, кроме указанного
        tags = Tag.objects.exclude(tag_name = 'адаптогены')
        print(tags)

# возвращает указанный тег
        tag1 = Tag.objects.get(tag_name__icontains = 'фитотерапия')
        print(tag1)

# Показывает статью, созданную последней по времени
        last_art = Article.objects.latest('article_data')
        print(last_art)

# Выводит статьи, начиная с пятой
        art2 = Article.objects.all()[4:]
        print(art2)

# сортируем статьи по алфавиту
        art_sort = Article.objects.order_by('article_name')
        print(art_sort)

# выводит все названия статей по указанному тегу
        art2_ = Article.objects.filter(article_tag__tag_name="фитотерапия")
        print(art2_)

# добавляем в базу данных
    #новый тег
        Tag.objects.create(tag_name = 'статьи')
        tags = Tag.objects.all()
        print(tags)

        t = Tag(tag_name = 'седативные')
        t.save()
        tags3 = Tag.objects.all()
        print(tags3)

    # новая статья (другие добавляются аналогично)
        a = Article.objects.create(article_name = 'Седативные', article_text = 'Описание, что это такое и список трав со ссылками', article_data = timezone.now())
        a.article_tag.add(t)
        articles = Article.objects.all()
        print(articles)

#удаление записей
        #tag = Tag.objects.filter(tag_name = 'Седативные')
        #tag.delete()
        #tags = Tag.objects.all()
        #print(tags)
