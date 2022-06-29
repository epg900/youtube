from django.urls import path
from . import views

urlpatterns = [
    path('', views.helping ),
    path('ytlink/', views.ytlink ),
    path('mp3/<str:link>', views.ytmp3 ),
    path('<str:link>/', views.ytdwn ),
]