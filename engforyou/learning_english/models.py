# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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



