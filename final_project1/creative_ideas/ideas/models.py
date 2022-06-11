from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    f_name = models.CharField(max_length=128)
    l_name = models.CharField(max_length=128)
    ideas = models.TextField(max_length=256 )
  # CHOICES =
   #(
    #    ('social', 'social'),
     #   ('profitability', 'profitability'),)

    cost = models.IntegerField(max_length=512)
    idea_owner=models.ForeignKey (User , on_delete=models.CASCADE)

class Comment(models.Model):
    f_name = models.CharField(max_length=128)
    l_name = models.CharField(max_length=128)
    ideas = models.ForeignKey (Profile , on_delete=models.CASCADE)
    comments = models.TextField(max_length=512)
    investor = models.ForeignKey (User , on_delete=models.CASCADE)
