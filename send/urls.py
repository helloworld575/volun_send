from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="send_index"),
    url(r'^password',views.set_password,name="set_password"),
    url(r'^set_password',views.set_password,name="set_password"),
    url(r'^stu_detail',views.stu_get_detail,name="student"),
    url(r'^tea_detail',views.teacher_get_detail,name="teacher"),
    url(r'^set_prot_password',views.email,name="email"),
    url(r'^tea_order_back',views.tea_order_back,name="tea_order_back"),
    url(r'^stu_order_back',views.stu_order_back,name="stu_order_back"),
]
