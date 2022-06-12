from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Business_idaea(models.Model):
    ideas = models.TextField(max_length=256 )
    type_idea=CHOISES=( ('social', 'social'),
                        ('profitability', 'profitability'))

    cost = models.IntegerField()
    idea_owner=models.ForeignKey (User , on_delete=models.CASCADE)

class Comment(models.Model):
    ideas = models.ForeignKey (Business_idaea, on_delete=models.CASCADE)
    comments = models.TextField(max_length=512)
    investor = models.ForeignKey (User , on_delete=models.CASCADE)
class Offers(models.Model):
    ideas = models.ForeignKey (Business_idaea, on_delete=models.CASCADE)
    offers = models.BooleanField()
    investor = models.ForeignKey (Comment , on_delete=models.CASCADE)

