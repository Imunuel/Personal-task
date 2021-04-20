from rest_framework import routers
from .views import QuestionViewSet

router = routers.SimpleRouter()

router.register(r'questions', QuestionViewSet, basename='Question')

urlpatterns = router.urls