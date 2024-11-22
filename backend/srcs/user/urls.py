from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='base'),
    re_path(r'^(?!static|admin|api).*/?$', index, name='index'),
]