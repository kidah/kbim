from django.urls import path, re_path

from . import views

app_name = 'kbim'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('details/api/<slug:api_name>', views.details, name='details'),
    path('chat/<slug:api_name>', views.chat, name='chatapi'),
    path('chatbot', views.get_message, name='chatbot'),
    path('authenticate', views.getAuthenticationCode, name='getcode'),
    path('oauth/callback', views.authenticate, name='authenticate'),
]