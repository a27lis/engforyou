from django.contrib import admin
from .models import Question, Quiz, Answer, Result


# Register your models here.
admin.site.register(Quiz)
admin.site.register(Result)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)