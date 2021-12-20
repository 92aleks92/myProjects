from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', RetroCarHome.as_view(), name='home'),  # подтягивает  пакет конфигураций urls.py с папки самого проекта
    path('cats/', about, name='about'),
    path('addpage/', AddPost.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]
