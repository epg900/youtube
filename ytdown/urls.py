from django.urls import path
from . import views

urlpatterns = [
    path('', views.helping ),
    path('ytlink/', views.ytlink ),
    path('<str:link>/', views.ytdwn ),
]