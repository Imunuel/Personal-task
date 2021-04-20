from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .serializer import HomeworkSerializer, HomeworkResultSerializer
from .models import Homework, HomeworkResult


class HomeworkResultViewSet(viewsets.GenericViewSet, viewsets.mixins.RetrieveModelMixin, viewsets.mixins.ListModelMixin):
    serializer_class = HomeworkResultSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('condition',)

    def get_queryset(self):
        return HomeworkResult.objects.all()