from django.urls import path
from .views import predict_sids_risk

urlpatterns = [
    path('predict/', predict_sids_risk),
]
