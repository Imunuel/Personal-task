from django.shortcuts import render
from .models import Answer, Question, TestTask, PersonalResult
from .serializer import AnswerSerializer, QuestionSerializer, TestTaskSerializer, PersonalResultSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets

# view для просмотра всех тестов, вопросов и ответов
class TestTaskViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.ListModelMixin):
    serializer_class = TestTaskSerializer

    def get_queryset(self):
        return TestTask.objects.prefetch_related('question').all()

# view для просмотра тестов, на которые ответил пользователь с его вариантом ответа
class PersonalResultViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.ListModelMixin):
    serializer_class = PersonalResultSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('condition',)

    def get_queryset(self):
        return PersonalResult.objects.prefetch_related('task').all()