from django.contrib import admin

# Register your models here.
from .models import Topic, Lesson, SpeakingTheme, Verb, Comment

admin.site.register(Topic)
admin.site.register(Lesson)
admin.site.register(SpeakingTheme)
admin.site.register(Verb)
admin.site.register(Comment)
