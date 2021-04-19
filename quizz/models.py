from django.db import models
import datetime
from django.contrib.auth.models import User


class Choice(models.Model):
    choice_text = models.CharField(max_length=25)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return self.question_text