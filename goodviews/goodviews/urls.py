"""
URL configuration for goodviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
#importing admin and include to later use to set up url pattern paths
from django.contrib import admin
from django.urls import include, path

#setting up url pattern routing. this helps the code to get information (from paths below) and display the website.
urlpatterns = [
    path('', include('media.urls')),
    path('admin/', admin.site.urls),
]