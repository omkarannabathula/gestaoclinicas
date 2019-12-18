from django.urls import path
from chatbot.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    path('', ChatterBotAppView.as_view(), name='main'),
    path('chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]