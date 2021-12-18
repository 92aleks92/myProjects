from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', RetroCarHome.as_view(), name='home'),  # подтягивает  пакет конфигураций urls.py с папки самого проекта
    path('cats/', about, name='about'),
    path('addpage/', AddPost.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]
