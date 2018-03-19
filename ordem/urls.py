from django.conf.urls import url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', views.ordem),
    url(r'^busca', views.busca),
    url(r'^abrir', views.abrir),
    url(r'^fechar', views.fechar),
    ]