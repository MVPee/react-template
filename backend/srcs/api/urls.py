from django.urls import path
from .views import *

urlpatterns = [
    path('views/home/', View.home, name='home_view'),
    path('views/about/', View.about, name='about_view'),
    path('views/contact/', View.contact, name='contact_view'),

    path('users/', get_users, name='get_all_users'),
    path('users/<int:pk>', get_user, name='get_user_by_id'),
    path('users/add/', add_user, name='add_user'),
]