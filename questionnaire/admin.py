from django.contrib import admin
from .models import Question, Answer, Skill

# Register your models here.
admin.site.register(Question)
admin.site.register(Skill)
admin.site.register(Answer)