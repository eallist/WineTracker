from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^buywine/', include('buywine.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
