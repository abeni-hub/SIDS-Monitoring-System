from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import joblib
import os

# Load model from the 'model' folder once at the top
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "sids_risk_detector.pkl")
model = joblib.load(model_path)


@api_view(['POST'])
def predict_sids_risk(request):
    try:
        # Extract incoming JSON data
        input_data = request.data

        # Expected input: a dict with the 5 required features
        required_fields = ['heart_rate', 'resp_rate', 'temperature', 'motion_duration', 'no_motion_duration']
        if not all(field in input_data for field in required_fields):
            return Response({'error': 'Missing one or more required fields.'}, status=400)

        df = pd.DataFrame([input_data])
        prediction = int(model.predict(df)[0])
        probability = float(model.predict_proba(df)[0][1])

        return Response({
            'risk': prediction,
            'probability': round(probability, 4)
        })

    except Exception as e:
        return Response({'error': str(e)}, status=500)
