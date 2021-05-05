"""webempresa URL Configuration

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
from django.urls import path, include
from core import urls as urls
from services import urls as urln
from django.conf import settings
from blog import urls as urlb
from pages import urls as urlp

urlpatterns = [
    path('admin/', admin.site.urls),
    #pathsCore
    path('', include(urls)),
    #pathsServices
    path('services/', include(urln)),
    #pathsBlog
    path('blog/', include(urlb)),
    #pathsBlog
    path('page/', include(urlp))

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
