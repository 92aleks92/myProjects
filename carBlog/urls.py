from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from carBlog import settings
from retroCar.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('retroCar.urls')),
]

if settings.DEBUG:
    import debug_toolbar #импорт в DTBUGе потому что вне его он не работает

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
# в режиме отладки когда DEBUG=True, к urlpatterns добавляется ещё один маршрут для статический данных и графических файлов
