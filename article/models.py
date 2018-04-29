from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    # if you don't right this you will see the object of article not the title of object
    def ___str__(self):
        return self.title

    def snippet(self):
        return self.body[:150]+'....'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,db_column='slug',default=None)


    def __str__(self):
        return self.text