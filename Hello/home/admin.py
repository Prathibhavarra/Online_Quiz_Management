from django.contrib import admin
from .models import *

# Register your models here.

class answersadmin(admin.StackedInline):
    model=answers

class questionsadmin(admin.ModelAdmin):
    inlines=[answersadmin]


admin.site.register(student)
admin.site.register(quiz_topic)
admin.site.register(questions ,questionsadmin)
admin.site.register(answers)
admin.site.register(feedback)