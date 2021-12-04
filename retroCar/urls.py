from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),  # подтягивает с пакета конфигураций urls.py с папки самого проекта
    path('cats/', categories, name='categories'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
