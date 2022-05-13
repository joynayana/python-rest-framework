"""rest URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapp.views import TaskViewset,CreateUserView
from restapp import views
# Create a router and register our viewsets with it.
# router=routers.DefaultRouter()
router=routers.SimpleRouter()
router.register('task_add',TaskViewset)
router.register('completed_task',views.completeTaskViewset)
router.register('Due_task',views.DueTaskViewset)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.CreateUserView.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',include(router.urls)),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)