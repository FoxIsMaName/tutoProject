from django.conf.urls import url

from . import views

app_name = 'ManMon'


urlpatterns = [

    url(r'^$', views.callMainPage, name="mainpage"),
    url(r'^accountInput$', views.callAccountInput, name="callAccountInput"),
    url(r'^saveAccount$', views.saveAccount, name="saveAccount"),
    url(r'^history$', views.history, name="history"),

]
