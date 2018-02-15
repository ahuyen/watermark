from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WatermarkUser(User):

    pass

class UserCard(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    owner = models.ForeignKey(WatermarkUser, on_delete=models.CASCADE)
    pass

class Wallet(models.Model):
    user = models.ForeignKey(WatermarkUser, on_delete=models.CASCADE)
    card = models.ForeignKey(UserCard, on_delete=models.CASCADE)
    pass