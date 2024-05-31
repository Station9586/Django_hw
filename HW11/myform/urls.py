"""
URL configuration for myform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from _myform.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index), 
    path("<int:pid>/<str:del_pass>/", index),
    path("list/", listing), 
    path("post/", posting), 
    path("contact/", contact), 
    path("post2db/", post2db), 
    re_path(r"^captcha/", include("captcha.urls")), 
    path("login/", login),
    path("logout/", logout),
    path("userinfo/", userinfo), 
    path("accounts/", include("registration.backends.default.urls")), 
]
