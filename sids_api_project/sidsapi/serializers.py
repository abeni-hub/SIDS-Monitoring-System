from rest_framework import serializers
from .models import PredictionRecord

class PredictionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionRecord
        fields = '__all__'
