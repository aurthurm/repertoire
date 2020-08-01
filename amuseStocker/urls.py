"""amuseStocker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from ajax_select import urls as ajax_select_urls
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ajax_select/', include(ajax_select_urls)),
    path('admin/', admin.site.urls),
    # path('accounts/login/', auth_views.login, name='login'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('', views.dashboard, name='dashboard'),
    path('help/', views.help_section, name='help-section'),
    path('help/settings', views.help_settings, name='help-settings'),
    path('help/dashboard', views.help_dashboard, name='help-dashboard'),
    path('help/suppliers', views.help_suppliers, name='help-suppliers'),
    path('help/inventory', views.help_inventory, name='help-inventory'),
    path('help/icons-and-colors', views.help_icons, name='help-icons'),
    path('contact-developer/', views.contact_developer, name='contact-developer'),
    path('movements/', include('movements.urls')),
    path('order/', include('order.urls')),
    path('basket/', include('basket.urls')),
    path('upload/', include('uploader.urls')),
    path('inventory/', include('products.urls')),
    path('laboratory/', include('laboratory.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
