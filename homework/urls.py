from rest_framework import routers
from .views import HomeworkResultViewSet, PersonalHomeworkViewSet

router = routers.SimpleRouter()

router.register(r'results', HomeworkResultViewSet, basename='Homework')# страница для мониторинга всех ДЗ и их фильтрации
router.register(r'myhomework', PersonalHomeworkViewSet, basename='personalHM')# страница для отправки ДЗ от пользователя

urlpatterns = router.urls