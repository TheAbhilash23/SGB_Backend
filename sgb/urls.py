"""SGBproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.base_items import BaseSwagger

from routers import router
from rendering_routers import router as rendering_router


urlpatterns = ([
    path('sgb/admin/', admin.site.urls),
    path('sgb/api/', include(router.get_urls()), name='api'),
    path('sgb/swagger/', include(BaseSwagger.urlpatterns)),
    path('sgb/render/', include(rendering_router.get_urls()), name='render'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
