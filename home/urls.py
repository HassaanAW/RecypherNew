import imp
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("logout", views.logout, name='logout'),
    path("team", views.team, name='team'),
    path("team/create", views.create_team, name='create_team'),
    path("team/join", views.join_team, name='join_team'),
    path("team/leaderboard", views.leaderboard, name='leaderboard'),
    path("team/info", views.team_info, name='team_info'),
    path("game", views.game, name='game'),
    path("game/scenario", views.scenario, name='scenario'),
    path("game/first_task", views.task_one, name='task_one'),
    path("game/first_task/email", views.email, name='email'),
    path("game/first_task/second_email", views.second_email, name='second_email'),
    path("game/second_task", views.task_two, name='task_two'),
    path("register", views.register, name='register'),

    path("game/second_task/e1", views.email_1, name='email_1'),
    path("game/second_task/ce2", views.email_2c, name='email_2c'),
    path("game/second_task/we2", views.email_2w, name='email_2w'),
    path("game/second_task/ce3", views.email_3c, name='email_3c'),
    path("game/second_task/we3", views.email_3w, name='email_3w'),
    path("game/second_task/ce4", views.email_4c, name='email_4c'),
    path("game/second_task/we4", views.email_4w, name='email_4w'),
    path("game/second_task/ce5", views.email_5c, name='email_5c'),
    path("game/second_task/we5", views.email_5w, name='email_5w'),
    path("game/second_task/ce6", views.email_6c, name='email_6c'),
    path("game/second_task/we6", views.email_6w, name='email_6w'),
    path("game/second_task/ce7", views.email_7c, name='email_7c'),
    path("game/second_task/we7", views.email_7w, name='email_7w'),
    path("game/second_task/ce8", views.email_8c, name='email_8c'),
    path("game/second_task/we8", views.email_8w, name='email_8w'),
    path("game/second_task/ce9", views.email_9c, name='email_9c'),
    path("game/second_task/we9", views.email_9w, name='email_9w'),
    path("game/second_task/ce10", views.email_10c, name='email_10c'),
    path("game/second_task/we10", views.email_10w, name='email_10w'),
    path("game/second_task/ce11", views.email_11c, name='email_11c'),
    path("game/second_task/we11", views.email_11w, name='email_11w'),
]
