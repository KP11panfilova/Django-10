"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views  # Импорт views из текущего приложения
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('home')
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("posts.urls")),
    path('articles/', include('articles.urls')),
    #path('', include('pages.urls')),
    #path('blog/', include('blog.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('posts/', include('posts.urls')),  # Маршрута для приложения posts
    path('', views.home, name='home'),  # Маршрута для главной страницы
    
]
from django.conf.urls import handler404, handler500

handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'