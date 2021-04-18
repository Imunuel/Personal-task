from rest_framework import routers
from .views import Question

router = routers.SimpleRouter()

router.register(r'questions', Question)

urlpatterns = router.urls