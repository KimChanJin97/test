from django.db.models.signals import post_save
from django.dispatch import receiver
from portfolio.models import Portfolio
from user.models import User


@receiver(post_save, sender=User)
def create_portfolio(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(user=instance)