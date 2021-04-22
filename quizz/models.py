from django.db import models
import datetime
from django.contrib.auth.models import User
'''
Для вопросов не были добавлены поинты с количеством баллов за ответ, так как опросник не подразумевает баллы за варианты
ответов и уж тем более правильность вариантов ответов
'''
# модель с вариантами ответов
class Choice(models.Model):
    choice_text = models.CharField(max_length=25)

    def __str__(self):
        return self.choice_text

# модель с вопросами и вариантами ответов для них
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return self.question_text