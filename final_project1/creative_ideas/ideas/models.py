from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Business_idaea(models.Model):
    '''
    idea owner add new idea , cost but must be register and login
    '''


    ideas = models.TextField(max_length=256 )
    cost = models.IntegerField()
    idea_owner=models.ForeignKey (User , on_delete=models.CASCADE)

    def __str__(self):

     return self.ideas

    class Meta :
        db_table='ideas_business_idaea'
        verbose_name="ideas"




class Comment(models.Model):
    '''
    the investor write comment in idea but must be register and login
    '''

    ideas = models.ForeignKey (Business_idaea, on_delete=models.CASCADE)
    comments = models.TextField(max_length=512)
    investor = models.ForeignKey (User , on_delete=models.CASCADE)

    def __str__(self):
        return self.comments




class Offers(models.Model):
    '''
    the owner of idea if offers true agree with investor if false reject with investor
    '''
    ideas = models.ForeignKey (Business_idaea, on_delete=models.CASCADE)
    offers_state = models.BooleanField()
    investor = models.ForeignKey (Comment , on_delete=models.CASCADE)

    def __str__(self):
        return self.ideas

