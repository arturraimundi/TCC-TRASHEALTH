"""
URL configuration for trashealth project.

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
from django.urls import include, path
from core.views import index, CadastrodePontos, vitrine, mapa, sac, login, perfil, register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', index),
    path('CadastrodePontos', CadastrodePontos, name='CadastrodePontos'),
    path('vitrine', vitrine, name='vitrine'),
    path('mapa', mapa, name='mapa'),
    path('sac', sac, name='sac'),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('perfil', perfil, name='perfil'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)