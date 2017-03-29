from django.conf.urls import url
from donations import views



urlpatterns = [
    url(r'^all', views.all_donations, name='donations'),
]
