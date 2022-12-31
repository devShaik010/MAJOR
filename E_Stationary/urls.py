from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from Ink_Spot import urls
from . import settings

urlpatterns = [
    path('',include('Ink_Spot.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
