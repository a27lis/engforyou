from django.db import models
from users.models import User

class Lesson(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    article = models.TextField()

    class Meta:
        managed = True
        db_table = 'lessons'

    def __str__(self):
        return self.title


class SpeakingTheme(models.Model):
    title = models.TextField()
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    
    class Meta:
        managed = True
        

    def __str__(self):
        return self.title
    
class Verb(models.Model):
    infinitive = models.TextField()
    second_form = models.TextField()
    third_form = models.TextField()
    translate = models.TextField()
    
    class Meta:
        managed = True
        

    def __str__(self):
        return self.infinitive
    

class Topic(models.Model):
    title = models.TextField()
    theme = models.TextField()
    article = models.TextField()
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    question_4 = models.TextField()
    question_5 = models.TextField()
    translate_1 = models.TextField()
    translate_2 = models.TextField()
    translate_3 = models.TextField()
    translate_4 = models.TextField()
    translate_5 = models.TextField()

    class Meta:
        managed = True
        db_table = 'topics'

    def __str__(self):
        return self.title
    
    def theme_as_title(self):
        return self.theme.split('-')


class Comment(models.Model):

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return self.text[:20]
