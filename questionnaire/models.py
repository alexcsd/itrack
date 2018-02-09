from django.db import models

# Create your models here.
class Question(models.Model):
    question_title  = models.CharField(max_length=250)
    nextTrue = models.CharField(blank=True, max_length=100)
    nextFalse = models.CharField(blank=True, max_length=100)
