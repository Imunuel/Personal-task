from rest_framework import serializers
from .models import Homework, HomeworkResult, PersonalHomework

'''
Связка обычных сериалайзеров нужна для показа всех ДЗ от всех пользователей и их фильторинга по состоянию ДЗ
'''
class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('homework_name', 'description')


class PersonalHomeworkSerializer(serializers.ModelSerializer):
    homework_task = HomeworkSerializer(read_only=False)

    class Meta:
        model = PersonalHomework
        fields = ('user', 'homework_task', 'homework_file')


class HomeworkResultSerializer(serializers.ModelSerializer):
    HM = PersonalHomeworkSerializer(read_only=False)
    class Meta:
        model = HomeworkResult
        fields = ('HM', 'mark', 'explanation', 'condition')

'''
Связка уникальных сериалайзеров нужна, для отдельного создания запроса в БД на создание ДЗ.
Такими сериалайзерами ограничивается видимость полей моделей для пользователя, оставляя лишь поля с названием ДЗ
и полем для выполненного ДЗ со стороны пользователя 
'''
class UniqueHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('homework_name',)


class UniquePersonalSerializer(serializers.ModelSerializer):
    homework_task = UniqueHomeworkSerializer
    class Meta:
        model = PersonalHomework
        fields = ('homework_task', 'homework_file')

# сериалазер для работы с загрузкой файла
class SpecialPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalHomework
        fields = ('homework_file',)