"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    # import应用的views文件，通过views添加路由
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    # import应用的views文件下的类，通过类添加路由
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    # 通过加载应用的子路由文件demo1.urls
    # 应用下的路由只管理自己的路由，结构层次清晰，不用担心重名，方便管理
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from demo1 import views
from demo1.views import article_detail

urlpatterns = [
    # django的内置应用
    path('admin/', admin.site.urls),
    # 此处的article_id与views文件中的article_id一一对应
    path('article/<int:article_id>', article_detail, name="article_detail")
    # 经试验，path不能像url那样有正则匹配的功能
    # path(r'home/', include('demo1.urls'))
]
