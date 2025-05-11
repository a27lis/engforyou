
from django import template
#from django.core.cache import cache
from django.conf import settings
import requests
import logging
import redis
import json

cache = redis.Redis.from_url('redis://localhost:6379/0')



register = template.Library()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@register.simple_tag(takes_context=True)
def get_recommendations(context):
    request = context['request']
    user_id = request.user.id
    
    # Пытаемся получить данные из кэша
    cache_key = 'user:1:recommendations'
    logger.info(cache_key)
    recommendations = cache.get(cache_key)
    logger.info("recomendations from cache: " + str(recommendations))
    cache.set('django', 'ok', 3600)
    if recommendations is None:
        try:
            # Если данных нет в кэше, делаем запрос к FastAPI
            response = requests.post(
                f"{settings.FASTAPI_URL}/recommendations/?user_id={user_id}",
                timeout=5
            )
            response.raise_for_status()            
            # Сохраняем результат в кэш
            recommendations = response.json()
            logger.info(str(recommendations))
        except Exception as e:
            # Логируем ошибку и возвращаем пустой список
            logger.error(f"Error getting recommendations: {str(e)}")
            return []
    loaded_recommendations = json.loads(recommendations.decode('utf-8'))
    return loaded_recommendations
