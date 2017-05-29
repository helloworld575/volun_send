from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="send_index"),
    url(r'^password',views.set_password,name="set_password"),
    url(r'^set_password',views.set_password,name="set_password"),
    url(r'^stu_detail',views.stu_get_detail,name="student"),
    url(r'^tea_detail',views.teacher_get_detail,name="teacher"),
    url(r'^tea_set_form',views.tea_set_form,name="tea_set_form"),
    url(r'^stu_get_form',views.stu_get_form,name="stu_get_form"),
    url(r'^set_prot_password',views.email,name="email"),
]
