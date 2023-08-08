from celery import shared_task
from datetime import date
from model.models.card_model import Cards


@shared_task
def freeze_expired_cards():
    today = date.today()
    expired_cards = Cards.objects.filter(expiry_date__gt=today, status='active')

    for card in expired_cards:
        card.status = 'frozen'
        card.save()
