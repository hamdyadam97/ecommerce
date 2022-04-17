from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from . import  views
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = [
    url(r'^$',views.checkout,name='checkout'),
    url(r'^orders$',views.orders,name='orders'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)