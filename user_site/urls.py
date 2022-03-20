from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.error_appearance, name='error_appearance'),
    url(r'^$', views.solution, name='solution'),
]