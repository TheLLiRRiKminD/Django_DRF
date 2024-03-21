from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone


@shared_task
def check_user_activity():
    user = get_user_model().objects.filter(is_active=True, last_login__lte=timezone.now() - timedelta(days=30))
    user.update(is_active=False)
