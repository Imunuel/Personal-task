from django.shortcuts import render
from .models import Answer, Question, TestTask
from .serializer import AnswerSerializer, QuestionSerializer, TestTaskSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets


class QuestionViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.ListModelMixin):
    # queryset = TestTask.objects.prefetch_related('question').all() #.prefetch_related('answers')
    serializer_class = TestTaskSerializer

    def get_queryset(self):
        return TestTask.objects.prefetch_related('question').all()

# filter_backends = (filters.DjangoFilterBackend,)
# filterset_fields = ('category', 'in_stock')