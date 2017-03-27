from django.conf.urls import url
from views import log_out, profile, log_in, register


urlpatterns = [
    url(r'^log_in$', log_in, name='log_in'),
    url(r'^register$', register, name='register'),
    url(r'^profile$', profile, name='profile'),
    url(r'^log_out$', log_out, name='log_out'),
]