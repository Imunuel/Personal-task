from django.db import models
from django.contrib.auth.models import User

# модель для создания всех вариантов ответов
class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

# модель для создания вопросов для теста
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answers = models.ManyToManyField(Answer, related_name='question')

    def __str__(self):
        return self.question_text

# модель для создания тестов с определенными вопросами, которые связанны с ответами
class TestTask(models.Model):
    task_name = models.CharField(max_length=100)
    sphere = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    question = models.ManyToManyField(Question)

    def __str__(self):
        data = (self.sphere, self.task_name)
        return ' | '.join(data)

# модель для вывода всех тестов, вопросов и выбранных вариантов ответов
class PersonalResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=[('rated', 'Rated'), 
                                        ('not_rated', 'Not Rated'), 
                                        ('done', 'Done'), 
                                        ('in_progress', 'In progress'),
                                        ('planned', 'Planned'),
                                        ('fail', 'Fail')])
            
    def __str__(self):
        data = (self.task.sphere, self.task.task_name, self.user.username)
        return ' | '.join(data)
    