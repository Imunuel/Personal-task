from django.contrib import admin
from .models import Answer, Question, TestTask, PersonalResult


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(TestTask)
admin.site.register(PersonalResult)