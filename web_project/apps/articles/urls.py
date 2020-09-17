"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

app_name = 'articles'  # создаем привязку к articles(*используется в list.html)
urlpatterns = [
    path('', views.index, name='index'),
    # path('test/', views.test, name = 'test')
    # приложение будет запоминать и использовать в дальнейшем id для ориентации
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment',
         views.leave_comment, name='leave_comment')
]
