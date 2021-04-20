from rest_framework import routers
from .views import QuestionViewSet

router = routers.SimpleRouter()

router.register(r'task_question', QuestionViewSet, basename='TestTask')

urlpatterns = router.urls