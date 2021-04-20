from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include


urlpatterns = [
    path('quizz/', include('quizz.urls')),
    path('task/', include('task.urls')),
    path('homework/', include('homework.urls')),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
]
