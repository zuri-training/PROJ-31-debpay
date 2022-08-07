from .models import*
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import (
    post_save,
    pre_save
) 

@receiver(post_save, sender=School)
def create_school_profile(sender, created, instance, *args, **kwargs):
    if created:
        School_Profile.objects.create(school=instance)
        
        
@receiver(post_save, sender=Debtor)
def create_debtor_profile(sender, created, instance, *args, **kwargs):
    if created:
        Deptors_profile.objects.create(debtor=instance)