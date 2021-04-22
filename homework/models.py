from django.db import models
from django.contrib.auth.models import User

# модель для создания ДЗ для пользователей
class Homework(models.Model):
    homework_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.homework_name

# модель для связывания пользователя, заданного ДЗ и его ответа
class PersonalHomework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    homework_task = models.ForeignKey(Homework, on_delete=models.CASCADE)
    homework_file = models.CharField(max_length=1) #файлы не подгружаются - пока не знаю как

    def __str__(self):
        data = (self.user.username, self.homework_task.homework_name)
        return ' | '.join(data)

# модель для результатирующих данных о всех ДЗ
class HomeworkResult(models.Model):
    HM = models.ForeignKey(PersonalHomework, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    explanation = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=[('done', 'Done'),('fail', 'Fail')])

    def __str__(self):
        data = (self.HM.user.username, self.HM.homework_task.homework_name)
        return ' | '.join(data)