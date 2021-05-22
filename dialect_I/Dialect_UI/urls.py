from django.urls import path
from . import views

urlpatterns = [
    path('', views.translator, name='translator'),
    path('translated/', views.translated, name='translated'),
    path('voice_recorder/', views.voice_rec, name='voice_rec'),
]