from django.urls import path
from .views import predict_sids_risk, get_latest_sids_data

urlpatterns = [
    path('predict/', predict_sids_risk),
    path('latest/', get_latest_sids_data),  # This is for your React frontend
]
