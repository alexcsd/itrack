from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.title + self.description

class Question(models.Model):
    Skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    body = models.TextField()
    body_ar = models.TextField()
    image = models.ImageField(blank=True)
    qtype = models.CharField(max_length=50) #TF & mcq  & meter/scale
    def __str__(self):
        return self.body

class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    body_ar = models.TextField()
    weight = models.FloatField()
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.body
