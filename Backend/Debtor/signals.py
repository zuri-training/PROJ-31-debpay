from .models import*
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import (
    post_save,
    pre_save
) 
user = get_user_model()

@receiver(post_save, sender=School)
def create_school_profile(sender, created, instance, *args, **kwargs):
    if created:
        School_Profile.objects.create(school=instance)
        
        
@receiver(post_save, sender = School)
def user_verification(sender, instance, created, *args, **kwargs):
    if created:
        UserVerification.objects.create(name = instance)