from rest_framework import serializers
from .models import Homework, HomeworkResult


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('homework_name', 'description')


class HomeworkResultSerializer(serializers.ModelSerializer):
    homework_task = HomeworkSerializer(read_only=False)

    class Meta:
        model = HomeworkResult
        fields = ('user', 'homework_task', 'homework_file', 'mark', 'explanation', 'condition')