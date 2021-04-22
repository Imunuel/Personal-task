from rest_framework import serializers
from .models import Answer, Question, TestTask, PersonalResult


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_text', 'is_correct')

# сериалайзер вопросов и связанных с ними ответов
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_text', 'answers')

# сериалайзер тестов, с полным набором вопросов и ответов к ним
class TestTaskSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = TestTask
        fields = ('sphere', 'points', 'question')

# результатирующие данные по тестам и юзерам
class PersonalResultSerializer(serializers.ModelSerializer):
    task = TestTaskSerializer
    answer = AnswerSerializer
    class Meta:
        model = PersonalResult
        fields = ('user', 'task', 'answer', 'condition')