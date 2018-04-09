from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    links= models.TextField(max_length=200 ,blank=True)
    def __str__(self):
        return self.title

# class ProfileCourse(models.Model):
#     course= models.ForeignKey(Course, on_delete=models.CASCADE)
#     profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
#     course_index= models.IntegerField(default=1)