from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import QuestionSerializer
from .models import Question, Choice

 
class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.prefetch_related('choices').all()