"""desy_r URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from reports import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^login/', views.login),
    url(r'^drives/$', views.display),
    url(r'^drive/create/$', views.create_drive),
    url(r'^drive/detail/(?P<pk>.*)/$', views.drive_detail),
    url(r'^drive/update/(?P<pk>.*)/$', views.update_drive),
    url(r'^drive/delete/(?P<pk>.*)/$', views.delete_drive),
    url(r'^students/(?P<pk>.*)/$'),
]
