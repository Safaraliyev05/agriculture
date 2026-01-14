import os

from celery import Celery
from prometheus_client import Counter

CELERY_TASKS_TOTAL = Counter(
    "celery_tasks_total",
    "Total Celery tasks executed",
    ["task_name", "status"]
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

app = Celery('root')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def send_email(self):
    try:
        CELERY_TASKS_TOTAL.labels(
            task_name="send_email",
            status="success"
        ).inc()
    except Exception:
        CELERY_TASKS_TOTAL.labels(
            task_name="send_email",
            status="failure"
        ).inc()
        raise
