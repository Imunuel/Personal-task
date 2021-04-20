from rest_framework import routers
from .views import HomeworkResultViewSet

router = routers.SimpleRouter()

router.register(r'results', HomeworkResultViewSet, basename='Homework')

urlpatterns = router.urls