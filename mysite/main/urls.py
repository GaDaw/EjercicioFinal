from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournament/<str:tournament_id>/', views.tournament, name='tournament'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('fighter/<str:fighter_id>/', views.fighter, name='fighter'),
    path('fighters/', views.fighters, name='fighters'),         
    path('tournament/new', views.tournament_new, name='tournament_new'),
    path('fighter/new', views.fighter_new, name='fighter_new'),
    path('initTournament', views.initTournament_new, name='initTournament'),
    path('disputedtournament/<str:dtournament_id>', views.disputedtournament, name='disputedtournament'),
    path('disputedtournaments/', views.disputedtournaments, name='disputedtournaments'),
    

    
    
]


