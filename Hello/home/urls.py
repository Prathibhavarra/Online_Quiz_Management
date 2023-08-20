from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('contact',views.contact, name="contact"),
    path('Login',views.Login,name="Login"),
    path('api/get-quiz/',views.get_quiz,name="get_quiz"),
    path('quiz/',views.quiz,name="quiz"),
    path('quizpage',views.quizpage,name="quizpage"),
    path('feed',views.feed,name="feed"),
]