from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'))
]

urlpatterns += static(settings.STATIC_URL, dokument_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, dokument_root=settings.MEDIA_ROOT)