from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="send_index"),
    url(r'^password',views.set_password,name="set_password"),
]
