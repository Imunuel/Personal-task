from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('quizz/', include('quizz.urls')),
    path('task/', include('task.urls')),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
]
