"""
URL configuration for mynewsite project.

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
from django.urls import path
from mysite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about), 
    path('list/', listing), 
    path('list/<str:sku>/', display_detail),
    path('', index), 
    path("<int:id>/<str:name>/<int:age>/", show, name = "list-url"), 
    path("<int:tvno>/", index, name = "tv-url"), 
    path("carlist/", carlist), 
    path("carlist/<int:maker>/", carlist, name = "carlist-url"), 
    path("carprice/", carprice), 
    path("carprice/<int:maker>/", carprice, name = "carprice-url"), 

]
