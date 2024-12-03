from django.db import models

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



