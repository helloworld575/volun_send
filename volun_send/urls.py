"""volun_send URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from send import urls as send_urls
from send import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^send/',include(send_urls)),
    url(r'^$',views.index,name="index"),
    url(r'^forget_password',views.forget_password,name="forget_password"),
    url(r'^signup',views.sign_up,name="signup"),
    url(r'^logout',views.log_out,name="log_out"),
]
