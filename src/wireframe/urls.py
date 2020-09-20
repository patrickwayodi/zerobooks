from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

# from django.conf.urls import include, url
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import include, path
# from django.views.generic import RedirectView


urlpatterns = [

    path('about/', views.about, name='about'),
    path('version/', views.project_version, name='project_version'),
    
    # url(r'^status/$', views.status, name='status'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^contact/$', views.contact, name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

