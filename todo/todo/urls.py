"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from firstapp.views import mainpage,registration,todo,detail,deletedata
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage.as_view(),name='index'),
    path('register/',registration,name='registration'),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    path('create/',todo,name='todo'),
    path('detail/<int:pk>/',detail,name="detail"),
    path('delete/<int:pk>/',deletedata,name='delete')
    
]