from django.urls import path
from .views import predict_sids_risk, get_latest_sids_data
from sidsapi import views

urlpatterns = [
    path('predict/', predict_sids_risk),
    path('latest/', get_latest_sids_data), 
    path('records/', views.all_predictions, name='all_predictions'),
 # This is for your React frontend
]
