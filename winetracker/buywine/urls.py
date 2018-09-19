from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save-new-wine-purchase$', views.save_new_wine_purchase, name='save-new-wine-purchase'),
    url(r'^find-wine$', views.find_wine, name='find-wine'),
    url(r'^display-wine-details$', views.display_wine_details, name='display-wine-details'),
    url(r'^save-wine-details$', views.save_wine_details, name='save-wine-details'),
    url(r'^explore-wine-collection$', views.save_wine_details, name='explore-wine-collection'),
]