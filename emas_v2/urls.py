"""emas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from user_site import views
import user_site
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from user_site.admin import error_detection_admin_site
from nlp_component.admin import feedback_app_admin_site


admin.site.name = "user_admin"

urlpatterns = [
    path('user_site/', include('user_site.urls')),
    path('user_admin/', admin.site.urls),
    path('error_detection_admin/', error_detection_admin_site.urls),
    path('feedback_admin/', feedback_app_admin_site.urls),
    path('index/', views.index, name='index'),
    path('error_appearance/<int:location>', views.error_appearance, name='error_appearance'),
    path('solution/', views.solution, name='solution'),
    path('rating/', views.rating, name='rating'),
    path('user_comment/', views.user_comment, name='user_comment'),
    path('pdf_locations/<int:location>', views.pdf_locations, name="pdf_locations"),
    path('search_process/', views.search_process, name="search_process"),
    path('change_language/', views.change_language, name="change_language"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


