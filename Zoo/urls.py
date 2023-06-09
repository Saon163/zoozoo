from django.urls import path
from .views import search

import Zoo.views

app_name = 'Zoo'

urlpatterns = [
    path('', Zoo.views.animal_list, name='animal_list'),
    path('zone/', Zoo.views.zone, name='zone'),
    path('detail/', Zoo.views.detail, name='detail'),
    path('update/<int:id>/', Zoo.views.animal_update, name = 'animal_update'),
    path('delete/<int:id>/', Zoo.views.animal_delete, name='animal_delete'),
    path('search', Zoo.views.search, name='search'),
]