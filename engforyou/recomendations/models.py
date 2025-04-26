from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    link = models.URLField(verbose_name="Ссылка")
    description = models.TextField(verbose_name="Описание")
    learning_style_V = models.BooleanField(default=False, verbose_name="Визуал")  # Визуальный
    learning_style_A = models.BooleanField(default=False, verbose_name="Аудиал")  # Аудиальный
    learning_style_R = models.BooleanField(default=False, verbose_name="Читатель/писатель")  # Чтение/Запись
    learning_style_K = models.BooleanField(default=False, verbose_name="Кинестетик")  # Кинестетический
    age_group_kid = models.BooleanField(default=False, verbose_name="Дети")     # Дети
    age_group_young = models.BooleanField(default=False, verbose_name="Подростки")   # Молодые
    age_group_student = models.BooleanField(default=False, verbose_name="Студенты") # Студенты
    age_group_adult = models.BooleanField(default=False, verbose_name="Взрослые")   # Взрослые
    age_group_mature = models.BooleanField(default=False, verbose_name="Зрелые")  # Зрелые
    
    def __str__(self):
        return self.title
