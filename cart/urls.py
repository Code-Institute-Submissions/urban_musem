from django.conf.urls import url
from views import cart_user, add_to_cart, remove_from_cart

urlpatterns = [
    url(r'^$', cart_user, name='cart_user'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove_from_cart')
]