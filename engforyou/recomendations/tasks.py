import requests
from celery import shared_task
import redis
from datetime import timedelta
from django.conf import settings


@shared_task(bind=True)
def update_recomendations(self):
	print("CELERY")
	try:
		response = requests.post(f"{settings.FASTAPI_URL}/recommendations/all",
                timeout=5)
		if response.status_code == 200:
			print("celery ok")
			return True
		return False
	except Exception as e:
		print(f"error: {str(e)}")
		self.retry(countdown=60)
