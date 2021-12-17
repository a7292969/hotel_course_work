from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms', views.rooms, name='rooms'),
    path('room', views.room, name='room'),
    path('reviews', views.reviews, name='reviews'),
    path('contacts', views.contacts, name='contacts'),
    path('send-comment', views.send_comment, name='send_comment'),
]
