from rest_framework import routers
from .views import TestTaskViewSet, PersonalResultViewSet

router = routers.SimpleRouter()

router.register(r'tasks', TestTaskViewSet, basename='TestTask')# страница со всеми тестами
router.register(r'result', PersonalResultViewSet, basename='PersonalResult')# страница с тестами с ответами юзеров

urlpatterns = router.urls