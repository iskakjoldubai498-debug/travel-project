from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# 1. Тил которуу механизми (негизги)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# 2. Тилге жараша өзгөрүүчү шилтемелер
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # Бардык логика ушул жерде
    prefix_default_language=True
)

# 3. Медиа жана статикалык файлдар
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)