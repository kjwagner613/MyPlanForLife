"""
URL configuration for myplanforlife project.

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
from mylife.views import HomeView
from django.contrib.auth.views import LogoutView
from mylife.views import custom_logout_view


urlpatterns = [
    path('accounts/logout/',LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),
    # path('accounts/logout/', custom_logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('mylife/', include('mylife.urls')),
    path('', HomeView.as_view(), name='home'),
]

handler400 = 'mylife.views.custom_400'
handler403 = 'mylife.views.custom_403'
handler404 = 'mylife.views.custom_404'


