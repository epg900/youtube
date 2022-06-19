from django.urls import path
from . import views

urlpatterns = [
    path('', views.helping ),
    path('<str:link>/', views.ytdwn ),
    path('ytlink/', views.ytlink ),
]