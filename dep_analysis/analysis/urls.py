from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_sentences, name='analyze_sentences'),
    path('analyze/', views.analyze_sentences, name='analyze_sentences'),
]
