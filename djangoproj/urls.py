from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from djangoproj import settings

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('favorites/', include('favorites.urls')),
    path('barbers/', include('barbers.urls'))
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)