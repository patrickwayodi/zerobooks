from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path

from csoon.views import ComingSoonView


urlpatterns = [
   
    # path('', ComingSoonView.as_view(), name='comingsoon'),       

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



'''sample code

path('', ComingSoonView.as_view(), name='comingsoon'),

# from django.conf.urls import include, url
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
# from django.urls import include, path
# from django.views.generic import RedirectView

# from . import views

# path('games-thanks/<int:slug>/', GamesThanksView.as_view(), name='games_thanks'),
# path('', views.homefeed, name='homefeed'),
# path('feed/', GameListView.as_view(), name='gamefeed'),
# path('feed/', views.homefeed, name='homefeed'),
# url(r'^feed/$', views.homefeed, name='homefeed'),
# url(r'^about/$', views.about, name='about'),

'''

