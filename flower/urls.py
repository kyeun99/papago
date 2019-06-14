"""flower URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', blog.views.blog, name="blog"),
    path('about/', blog.views.about, name="about"),
    path('blog/<int:blog_id>', blog.views.blogdetail, name="blogdetail"),
    path('blog/new/', blog.views.blognew, name='blognew'),
    path('blog/create/', blog.views.blogcreate, name='blogcreate'),
    path('blog/<int:blog_id>/comment', blog.views.blogcomment_new, name="blogcomment_new"),
    path('alog/', blog.views.alog, name="alog"),
    path('alog/<int:alog_id>', blog.views.alogdetail, name="alogdetail"),
    path('alog/new/', blog.views.alognew, name='alognew'),
    path('alog/create/', blog.views.alogcreate, name='alogcreate'),
    path('alog/<int:alog_id>/comment', blog.views.alogcomment_new, name="alogcomment_new"),
    path('clog/', blog.views.clog, name="clog"),
    path('clog/<int:clog_id>', blog.views.clogdetail, name="clogdetail"),
    path('clog/new/', blog.views.clognew, name='clognew'),
    path('clog/create/', blog.views.clogcreate, name='clogcreate'),
    path('clog/<int:clog_id>/comment', blog.views.clogcomment_new, name="clogcomment_new"),
    path('account/', include('account.urls')),
]
