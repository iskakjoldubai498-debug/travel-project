from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Тилге карабаган шилтемелер
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Тилге караган шилтемелер (Кыргызча/Орусча)
urlpatterns += i18n_patterns(
    path('', include('main.urls')),
)

# Бул бөлүм СӨЗСҮЗ эң аягында болушу керек
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)