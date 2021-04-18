from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import QuestionSerializer
from .models import Question, Choice, Answer


class Question(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]