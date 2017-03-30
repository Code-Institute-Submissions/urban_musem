from django.conf.urls import url
from museums.views import my_museums, museum_detail, add_museum, edit_museum, remove_museum, add_piece_to_museum, pieces_details, edit_piece, remove_piece

urlpatterns = [
    url(r'^new/', add_museum, name='add_musuem'),
    url(r'^(?P<id>\d+)/remove/', remove_museum, name='remove_museum'),
    url(r'^(?P<id>\d+)/edit/', edit_museum, name='edit_museum'),
    url(r'^(?P<id>\d+)/piece/add/', add_piece_to_museum, name="add_piece_to_museum"),
    url(r'^(?P<id>\d+)/piece/details/', pieces_details, name="pieces_details"),
    url(r'^(?P<id>\d+)/piece/edit/', edit_piece, name="edit_piece"),
    url(r'^(?P<id>\d+)/piece/remove/', remove_piece, name='remove_piece_from_museum'),
    url(r'^(?P<id>\d+)/$', museum_detail, name="museum_detail"),
    url(r'^$', my_museums, name="my_museums"),
]