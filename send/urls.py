from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="send_index"),
    url(r'^password',views.set_password,name="set_password"),
    url(r'^set_password',views.set_password,name="set_password"),
    url(r'^stu_detail',views.stu_get_detail,name="student"),
    url(r'^set_prot_password',views.email,name="email"),
]
