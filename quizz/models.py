from django.db import models
import datetime
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=25)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username