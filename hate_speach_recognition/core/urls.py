from django.urls import path
from . import views

urlpatterns = [
    path('predict_hate_speech/', views.predict_hate_speech, name='predict_hate_speech'),
    # Add other URL patterns for the core app here
]
