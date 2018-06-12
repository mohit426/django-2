from django.contrib.urls import url
from . import views

urlpatterns = [
	url(r'^list/$', views.music, name="music"),
	url(r'^(?<pk>[0-9]+)/$',views.listening, name="list_song"),
	]
