from django.conf.urls import url
from museums.views import my_museums, museum_detail, add_museum, edit_museum, remove_museum

urlpatterns = [
    url(r'^new/', add_museum, name='add_musuem'),
    url(r'^my_museums/(?P<id>\d+)/remove/', remove_museum, name='remove_museum'),
    url(r'^my_museums/(?P<id>\d+)/edit/', edit_museum, name='edit_museum'),
    url(r'^my_museums/(?P<id>\d+)/', museum_detail, name="museum_detail"),
    url(r'^my_museums/', my_museums, name="my_museums"),
]