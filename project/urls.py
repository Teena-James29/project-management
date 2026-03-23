"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',homefn),
    path('signup/', signupfn),
    path('projectcreate/', projectcreatefn),
    path('projectlist/', projectlistfn),
    path('projectupdate/<int:id>/', projectupdatefn),
    path('projectdelete/<int:id>/', projectdeletefn),
    path('submittask/<int:id>/', submittask),
    path('taskcreate/', taskcreatefn),
    path('taskupdate/<int:id>/', taskupdatefn),
    path('taskdelete/<int:id>/', taskdeletefn),
    path('tasklist/', tasklistfn),
    path('calendar/',calendarview),
    path('report/',reportview),
    path('mytasks/',mytasks),

    

    path('clientlist/', clientlistfn), 
    path('clientcreate/',clientcreatefn),
    path('clientupdate/<int:id>/', clientupdatefn),
    path('clientdelete/<int:id>/',clientdeletefn),
    path('', loginfn),
    path('logout/', logoutfn),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

