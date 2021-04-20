from rest_framework import routers
from .views import TestTaskViewSet, PersonalResultViewSet

router = routers.SimpleRouter()

router.register(r'tasks', TestTaskViewSet, basename='TestTask')
router.register(r'result', PersonalResultViewSet, basename='PersonalResult')

urlpatterns = router.urls