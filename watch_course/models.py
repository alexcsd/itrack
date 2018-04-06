from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    links= models.TextField(max_length=200 ,blank=True)
    def __str__(self):
        return self.title
