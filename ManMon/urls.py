from django.conf.urls import url

from . import views

app_name = 'ManMon'


urlpatterns = [

    url(r'^$', views.callMainPage, name="callMainPage"),

]
