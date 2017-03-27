from django.conf.urls import url
from views import log_out, profile, log_in


urlpatterns = [
    url(r'^log_in$', log_in, name='log_in'),
    url(r'^profile$', profile, name='profile'),
    url(r'^log_out$', log_out, name='log_out'),
]