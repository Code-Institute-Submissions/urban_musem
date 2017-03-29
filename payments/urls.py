from django.conf.urls import url
from .views import support_us

urlpatterns = [
    url(r'^thanks_for/(?P<id>\d+)', support_us, name='support_us'),
]