from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
    (0, 'Femme'),
    (1, 'Homme'),
)

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    genre = models.PositiveBigIntegerField(choices=GENDER, null=True)
    age = models.PositiveBigIntegerField(null=True)
    Tension = models.PositiveBigIntegerField(null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_avc_model.joblib')
        self.predictions = ml_model.predict([[self.genre, self.age, self.Tension]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
        
