from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from feed.views import ChronoFeedTemplateView


urlpatterns = [

    path('', ChronoFeedTemplateView.as_view(), name='chrono_feed'),

    # path('chronofeed/', ChronoGameListView.as_view(), name='chronofeed'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# from django.conf.urls import include, url
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import include, path
# from django.views.generic import RedirectView

# from . import views


# path('feed/', GameListView.as_view(), name='homefeed'),
# path('', views.homefeed, name='homefeed'),
# path('feed/', GameListView.as_view(), name='gamefeed'),
# path('', GameListView.as_view(), name='homefeed'),
# path('feed/', views.homefeed, name='homefeed'),
# url(r'^feed/$', views.homefeed, name='homefeed'),
# url(r'^about/$', views.about, name='about'),

