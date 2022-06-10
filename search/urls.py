from django.urls import path
from . import views

urlpatterns = [
    path('search', views.index, name='index'),
    path('word', views.word, name='word'),
    path('contact', views.contact,name ='contact'),
    path('about', views.about,name ='about'),
]
