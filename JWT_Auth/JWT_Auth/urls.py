"""JWT_Auth URL Configuration

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
from django.urls import path,include
from JWT_app import views
from JWT_app.views import Student_view
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Student_details',views.Student_view)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('one/',include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('second/',TokenRefreshView.as_view()),
    path('three/',TokenVerifyView.as_view())

]
