from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /places/
    url(r'^$', views.get_places, name='index'),
]