from django.conf.urls.static import static
from django.urls import path

from backend import settings
from products import views

urlpatterns = [
    path('', views.products_display, name='products_display')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
