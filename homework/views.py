from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import request
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializer import HomeworkSerializer, 
                        HomeworkResultSerializer, 
                        PersonalHomeworkSerializer, 
                        UniquePersonalSerializer,
                        SpecialPersonalSerializer
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
        return HomeworkResult.objects.prefetch_related('HM').all()

# Страница со всеми ДЗ, которые относятся к текущему юзеру
class PersonalHomeworkViewSet(viewsets.GenericViewSet, 
                                viewsets.mixins.RetrieveModelMixin, 
                                viewsets.mixins.ListModelMixin, 
                                viewsets.mixins.UpdateModelMixin,
                                viewsets.mixins.CreateModelMixin):
    serializer_class = UniquePersonalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PersonalHomework.objects.prefetch_related('homework_task').filter(user=self.request.user)
    
    '''
    метод для обработки данных
    Не уверен можно ли это считать загрузкой файла - по сути мы открываем файл и берем из него даннеы,
    а позже записываем данные в поле 
    '''
    @action(method=['POST'], detail=True)
    def upload(self, request):
        serializer = SpecialPersonalSerializer
        file = serializer.data
        file_data=[]
        with open(file, 'r'):
            for lines in file:
                file_data.append(lines)
        PersonalHomework.homework_file = file_data
        PersonalHomework.save()