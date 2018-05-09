from django.conf.urls import url
from . import views,tests


urlpatterns = [
    url(r'^regist', views.Regist, name='regist'),
    url(r'^write', views.Write, name='write'),
    url(r'^qrangking', views.Q_rangking, name='qranging'),
    url(r'^getopenid', views.Get_openid, name='getopenid'),
    ]

