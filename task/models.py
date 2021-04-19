from django.db import models


class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question_text


class TestTask(models.Model):
    sphere = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.sphere