from django.urls import path
from Zoo import views

app_name = 'animals'
urlpatterns = [
    path('', views.zkp_main, name='zkp_main'),
    path('animal_detail/<str:anm_spcs>/', views.animal_detail, name='animal_detail'),
    path('<str:anm_spc>/zone/', views.animal_zone, name='animal_zone'),
]
