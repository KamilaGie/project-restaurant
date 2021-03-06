"""project URL Configuration

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
from restaurant.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$', HomeView.as_view(), name = 'home'),
    url(r'^home/(?P<c>(\w)+)$', CategoryView.as_view(), name = 'category'),
    url(r'^$', LoginView.as_view(), name= 'login'),
    url(r'^logout$', LogoutView, name = 'logout'),
    url(r'^home/(?P<c>(\w)+)/(?P<p>(\w)+)$', OrderView.as_view(), name='order'),
    url(r'^kitchen$', KitchenView.as_view(), name='kitchen'),
    url(r'^bar$', BarView.as_view(), name='bar'),


]
