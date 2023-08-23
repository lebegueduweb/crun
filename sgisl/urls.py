"""
URL configuration for sgisl project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
# Use include() to add paths from the labapp application
# Use RedirectView to root the site to the only app labapp
# Use static() to add url mapping to serve static files during development (only)
    path('labapp/', include('labapp.urls')),
    path('', RedirectView.as_view(url='/labapp/', permanent=True)),
    path('admin/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
admin.site.site_header = "CRUN administration"
admin.site.site_title = "Système de gestion informatisée des laboratoire IRSS-DRCO"
admin.site.index_title = "Bienvenue à IRSS-DRCO"