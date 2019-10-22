"""tax_backend URL Configuration

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
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^location/$', views.location, name='location'),
    url(r'^supervisor/$', views.supervisor, name='supervisor'),
    url(r'^add/business', views.add_business, name='add_business'),
    url(r'^add/location', views.add_location, name='add_location'),
    url(r'^update/location', views.update_location, name='update_location'),
    url(r'^add/supervisor', views.add_supervisor, name='add_supervisor'),
    url(r'^update/supervisor', views.update_supervisor, name='update_supervisor'),
    url(r'^approve/supervisor', views.approve_supervisor, name='approve_supervisor'),
    url(r'^suspend/supervisor', views.suspend_supervisor, name='suspend_supervisor'),
    url(r'^add/admin/$', views.add_admin, name='add_admin'),
    url(r'^add/category', views.add_category, name='add_category'),
    url(r'^update/category', views.update_category, name='update_category'),
    url(r'^update/business', views.update_business, name='update_business'),
    url(r'^business/category/$', views.business_category, name='business_category'),
    url(r'^business/$', views.business, name='business'),
    url(r'^administrator/$', views.administrator, name='administrator'),
]
