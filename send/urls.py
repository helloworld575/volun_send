from django.conf.urls import include,url
from . import views

urlpatterns=[
    url(r'^$',views.index,name="send_index"),
    url(r'^logout',views.log_out,name="log_out"),
    url(r'^password',views.set_password,name="set_password"),
    url(r'^set_password',views.set_password,name="set_password"),
    url(r'^stu_detail',views.stu_get_detail,name="student"),
    url(r'^tea_detail',views.teacher_get_detail,name="teacher"),
    url(r'^tea_set_form',views.tea_set_form,name="tea_set_form"),
    url(r'^stu_get_form',views.stu_get_form,name="stu_get_form"),
    url(r'^set_prot_password',views.email,name="email"),
    url(r'^illustration',views.illustration,name="illustration"),
    url(r'^detail_student',views.detail_student,name="detail_student"),
    url(r'^detail_teacher',views.detail_teacher,name="detail_teacher"),
    url(r'^modify_student',views.modify_student,name="modify_student"),
    url(r'^modify_teacher',views.modify_teacher,name="modify_teacher"),
]
