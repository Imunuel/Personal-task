from django.contrib import admin
from .models import Homework, HomeworkResult, PersonalHomework


admin.site.register(Homework)
admin.site.register(HomeworkResult)
admin.site.register(PersonalHomework)