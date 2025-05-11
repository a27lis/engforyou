import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engforyou.settings')

app = Celery('engforyou')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


#@app.on_after_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
#    sender.add_periodic_task(
#        '*/1 * * * *',  # каждую минуту
#        update_recommendations.s(),
#        name='update-recomendations'
#    )