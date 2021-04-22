from rest_framework import serializers
from .models import Question, Choice

#сериалайзеры для связывания данных вопроса и данных ответа
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('question_text', 'choices')