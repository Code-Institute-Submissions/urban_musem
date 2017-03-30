from django.conf.urls import url
from pieces.views import pieces_list, pieces_details, add_piece, edit_piece, remove_piece

urlpatterns = [
    url(r'list/', pieces_list, name='pieces_list'),
    url(r'^add_piece/', add_piece, name='add_piece'),
    url(r'^(?P<id>\d+)/edit/', edit_piece, name='edit_piece'),
    url(r'^(?P<id>\d+)/details/', pieces_details, name='piece_details' ),
    url(r'^(?P<id>\d+)/remove/', remove_piece, name='remove_piece'),

]
