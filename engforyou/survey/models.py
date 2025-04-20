from django.db import models
from users.models import User

class LearningStyle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    visual_percent = models.FloatField(
        verbose_name='Визуал',
        null=True,
        blank=True
    )
    audio_percent = models.FloatField(
        verbose_name='Аудиал',
        null=True,
        blank=True
    )
    reader_percent = models.FloatField(
        verbose_name='Читатель-писатель',
        null=True,
        blank=True
    )
    kinesthetic_percent = models.FloatField(
        verbose_name='Кинестетик',
        null=True,
        blank=True
    )
    
    primary_style = models.CharField(
        verbose_name='Основной стиль обучения',
        max_length=50,
        null=True,
        blank=True
    )
    secondary_style = models.CharField(
        verbose_name='Второстепенный стиль обучения',
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Стили обучения для пользователя {self.user.username}'


