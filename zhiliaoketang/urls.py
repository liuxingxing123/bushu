"""zhiliaoketang URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from news import views as news_view
from django.views import static  ##新增
from django.conf import settings  ##新增

# https://gitee.com/hynever/zhiliaoketang.git

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', news_view.index, name='index'),
    url(r'^an/$', news_view.add_news, name='add_news'),
    url(r'^nd/<news_id>/$', news_view.add_news, name='add_news'),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'),

]
