from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class WatermarkUser(User):

    pass

class UserCard(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    owner = models.ForeignKey(WatermarkUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, default='Default text.')
    pass

class Wallet(models.Model):
    user = models.OneToOneField(WatermarkUser, on_delete=models.CASCADE)
    card = models.ManyToManyField(UserCard)
    pass

class Profile(models.Model):
    user = models.OneToOneField(WatermarkUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=10000)
    pass


@receiver(post_save, sender=WatermarkUser)
def user_saved(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.create(user=instance)
        profile = Profile.objects.create(user=instance)
        profile.bio = "Default text for profile bio."
        print("An instance of WatermarkUser was created.")
    else:
        instance.save()
