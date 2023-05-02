from django.contrib import admin
from .models import Question, choices


admin.site.register(Question)
admin.site.register(choices)
