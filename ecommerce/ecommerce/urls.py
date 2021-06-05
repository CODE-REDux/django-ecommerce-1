from django.contrib import admin
from django.urls import path, include
# imports static function to set MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# we grab settings.MEDIA_URL and setting its value to document_root=settings.MEDIA_ROOT
