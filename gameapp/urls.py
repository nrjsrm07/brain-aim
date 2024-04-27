from django.urls import path
from django.contrib import admin
from gameapp import views

urlpatterns = [
    path('',views.home_view, name='startgame'),
    path('WelcomePage.html',views.home_view ),
    path('QuestionPage.html',views.question_view ),
    path('AddQuestion.html',views.add_question_view ),
    path('add_question',views.add_question ),
    path('truth_dare_view',views.truth_dare_view ),
]