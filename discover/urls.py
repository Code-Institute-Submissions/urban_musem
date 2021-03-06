from django.conf.urls import url
from discover.views import get_discover, get_result, latest_places, most_viewed, museum_user


urlpatterns = [
    url(r'^user/(?P<id>\d+)', museum_user, name='museum_user'),
    url(r'^result/', get_result, name='get_result'),
    url(r'^latest/', latest_places, name='latest_places'),
    url(r'^popular/', most_viewed, name='most_viewed'),
    url(r'^$', get_discover, name="get_discover" )
]