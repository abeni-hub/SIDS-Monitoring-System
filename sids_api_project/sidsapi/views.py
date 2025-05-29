from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import joblib
import os
from django.http import JsonResponse
from .models import PredictionRecord
from .serializers import PredictionRecordSerializer

# Load model from the 'model' folder once at the top
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "sids_risk_detector.pkl")
model = joblib.load(model_path)

# Store the latest data and prediction for GET access
latest_data = {}

@api_view(['POST'])
def predict_sids_risk(request):
    global latest_data
    try:
        # Extract incoming JSON data
        input_data = request.data

        # Expected input: a dict with the 4 required features (without 'resp_rate')
        required_fields = ['heart_rate', 'temperature', 'motion_duration', 'no_motion_duration']
        if not all(field in input_data for field in required_fields):
            return Response({'error': 'Missing one or more required fields.'}, status=400)

        df = pd.DataFrame([input_data])
        prediction = int(model.predict(df)[0])
        probability = float(model.predict_proba(df)[0][1])

        # Save latest input and prediction
        latest_data = {
            'input': input_data,
            'risk': prediction,
            'probability': round(probability, 4)
        }

        return Response(latest_data)

    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def get_latest_sids_data(request):
    if latest_data:
        return Response(latest_data)
    else:
        return Response({'message': 'No data available yet.'})


def all_predictions(request):
    records = PredictionRecord.objects.all()
    serializer = PredictionRecordSerializer(records, many=True)
    return Response(serializer.data)