from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('card/', card, name='card'),
    path('orki/', orki, name='orki'),
    path('add_ork/', add_ork, name='add_ork'),
    path('rem_ork/', rem_ork, name='rem_ork'),
]
