"""iam URL Configuration

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
from django.utils.translation import gettext_lazy as _

from routers import router

import admin as django_admin_portal
from rest_social_providers.views import GoogleLogin

admin.site.login = django_admin_portal.CustomBackendLoginView.as_view(template_name='admin/SelfMade_Login.html')
admin.site.site_header = _('IAM')

# class CustomAdminSite(AdminSite):
#     login_template = 'admin/login.html'
#     site_header = gettext_lazy("IAM")
#
#
# admin_site = CustomAdminSite()
# admin.site = CustomAdminSite(name=admin_site.name)
# admin.site.register(admin_site._registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.get_urls()), name='api'),
    path('api/o/', include('dj_rest_auth.urls')),
    path('api/o/registration/', include('dj_rest_auth.registration.urls')),
    path('api/o/google/', GoogleLogin.as_view(), name='dj_google_login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# from dj_rest_auth.registration.urls import
