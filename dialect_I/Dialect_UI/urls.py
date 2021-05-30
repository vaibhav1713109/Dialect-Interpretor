from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('translator/', views.translator, name='translator'),
    path('translated/', views.translated, name='translated'),
    path('voice_recorder/', views.voice_rec, name='voice_rec'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
]