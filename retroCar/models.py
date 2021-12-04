from django.db import models

from django.urls import reverse


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # метод формирует нужный маршрут, маршрут к конкретной записи
        return reverse('category', kwargs={'cat_id': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(blank=True,
                              upload_to="photos/%Y/%m/%d/")  # upload_to указывает на то в какой катало/подкаталог
    # будем загружать фото
    content = models.TextField(verbose_name='КОНТЕНТ')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    time_create = models.DateTimeField(
        auto_now_add=True)  # auto_now_add принимает текущие время в момент добавления новой записи
    time_update = models.DateTimeField(auto_now=True)  # auto_now меняется каждый раз

    def __str__(self):
        return self.title  # метод выводит полный заголовок title при работе таблицами в shell

    def get_absolute_url(self):  # метод формирует нужный маршрут, маршрут к конкретной записи
        return reverse('post', kwargs={'post_id': self.pk})
