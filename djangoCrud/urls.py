"""
URL configuration for djangoCrud project.

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
from django.urls import include, path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.createTask, name='createTask'),
    path('logout/', views.signout, name='logout'),
    path('homeAdmin/', views.homeAdmin, name='homeAdmin'),
    path('homePsicologo/', views.homePsicologo, name='homePsicologo'),
    path('fichaIdentidad/', views.fichaIdentidad, name='fichaIdentidad'),
    path('agendarCita/', views.agendarCita, name='agendarCita'),
]