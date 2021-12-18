from django.contrib import admin

from retroCar.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'time_update')
    # поля которые будет отображаться в админке
    list_display_links = ('id', 'title')  # содержит те поля на которые можно перейти
    search_fields = ('id', 'title')  # по каким полям можно производить поиск
    list_filter = ('time_create',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = (
        'title',)  # обязательно ставить запятую так как должны передовать кортеж без запятой это будет строка
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
