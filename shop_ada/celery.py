import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_ada.settings')

app = Celery('shop_ada')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.conf.broke_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()