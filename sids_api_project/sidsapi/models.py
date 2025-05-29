
# Create your models here.
from django.db import models

class PredictionRecord(models.Model):
    heart_rate = models.IntegerField()
    temperature = models.FloatField()
    motion_duration = models.IntegerField()
    no_motion_duration = models.IntegerField()
    risk = models.IntegerField()
    probability = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - Risk: {self.risk} ({self.probability})"
