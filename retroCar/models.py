from django.db import models

from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # метод формирует нужный маршрут, маршрут к конкретной записи
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:  # вложенный класс который используется для настройки основной модели
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'  # меня окончание в админке с множественного числа на единственное
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(blank=True,
                              upload_to="photos/%Y/%m/%d/",
                              verbose_name='Фото')  # upload_to указывает на то в какой каталог/подкаталог
    # будем загружать фото
    content = models.TextField(verbose_name='Текст статьи')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, verbose_name="Категории")
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания')  # auto_now_add принимает текущие время в момент добавления новой записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')  # auto_now меняется каждый раз

    def __str__(self):
        return self.title  # метод выводит полный заголовок title при работе таблицами в shell

    def get_absolute_url(self):  # метод формирует нужный маршрут, маршрут к конкретной записи
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:  # вложенный класс который используется для настройки основной модели
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'  # меня окончание в админке с множественного числа на единственное
        ordering = ['id']  # сортировка по полям
