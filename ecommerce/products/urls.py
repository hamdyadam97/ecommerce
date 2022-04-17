from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from . import  views
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = [
    url(r'^products/$',views.all,name='products'),
    url(r'^search/$',views.search,name='search'),
    url(r'^products/(?P<slug>[\w-]+)/$',views.single,name='single'),
    url(r'^$',views.home,name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)