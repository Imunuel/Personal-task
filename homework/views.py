from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import request
from .serializer import HomeworkSerializer, HomeworkResultSerializer, PersonalHomeworkSerializer, UniquePersonalSerializer
from .models import Homework, HomeworkResult, PersonalHomework

'''
ViewSets для просмотра всех ДЗ и фильторинга, а так же для отправки ДЗ пользователем 
'''
class HomeworkResultViewSet(viewsets.GenericViewSet, 
                            viewsets.mixins.RetrieveModelMixin, 
                            viewsets.mixins.ListModelMixin):
    serializer_class = HomeworkResultSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('condition',)

    def get_queryset(self):
        return HomeworkResult.objects.prefetch_related('HM').select_related('HM').all()


class PersonalHomeworkViewSet(viewsets.GenericViewSet, 
                                viewsets.mixins.RetrieveModelMixin, 
                                viewsets.mixins.ListModelMixin, 
                                viewsets.mixins.CreateModelMixin):
    serializer_class = UniquePersonalSerializer

    def get_queryset(self):
        return PersonalHomework.objects.prefetch_related('homework_task').all()
        # return PersonalHomework.objects.prefetch_related('homework_task').filter()