from django.contrib import admin

from .models import Exam, Lecture, Workshop

admin.site.register(Exam)
admin.site.register(Lecture)
admin.site.register(Workshop)
