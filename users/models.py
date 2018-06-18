from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from watch_course.models import Course

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    img_src= models.ImageField(upload_to='profiles/images/', default='sampleavatar.png', blank=True)
    course= models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    course_index= models.IntegerField(default=1)
    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
