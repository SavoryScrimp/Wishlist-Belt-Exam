from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.index),
    url(r'^create$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^addItem$', views.addItem),
    url(r'^createItem$', views.createItem),
    url(r'^delete/(?P<number>\d+)$', views.deleteItem),
    url(r'^addList/(?P<number>\d+)$', views.addList),
    url(r'^removeList/(?P<number>\d+)$', views.removeList),
    url(r'^wish_items/(?P<number>\d+)$', views.itemView),
]