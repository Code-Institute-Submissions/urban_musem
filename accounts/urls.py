from django.conf.urls import url
from views import log_out, profile, log_in, register, remove_account
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url(r'^log_in$', log_in, name='log_in'),
    url(r'^register$', register, name='register'),
    url(r'^profile$', profile, name='profile'),
    url(r'^log_out$', log_out, name='log_out'),
    url(r'^remove/(?P<id>\d+)$',remove_account, name='remove_account'),
    url(r'^password/reset/$', password_reset, {'post_reset_redirect': '/user/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', password_reset_done, name='password_reset_done'),
        url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {'post_reset_redirect': '/user/password/done/'}, name='password_reset_confirm'),
    url(r'^password/done/$', password_reset_complete, name='password_reset_complete'),
]