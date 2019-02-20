"""HRDepartment URL Configuration

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
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
  
    path('admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    #url(r'^$', views.IndexView.as_view(), name='home'), 
    url(r'^hro/', include('hro.urls', namespace='hro')),
    #url(r'^$', views.index,name='index'),
        #This connect account to django authentication urls and model
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^thanks/$', views.ThanksPage.as_view(), name="thanks"),
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^advice/$', views.Advice.as_view(), name='advice'),
]

#For enabling debug mode
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),

#         # For django versions before 2.0:
#         # url(r'^__debug__/', include(debug_toolbar.urls)),

#     ] + urlpatterns