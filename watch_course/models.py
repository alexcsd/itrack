from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    link= models.CharField(max_length=50)
    def __str__(self):
        return self.title + self.link
