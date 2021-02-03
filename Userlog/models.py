from django.db import models

# Create your models here.

#first create the class

class UserTopic(models.Model):
    #User interest
    text = models.CharField(max_length=200) #we want to display characters with max 250
    date_uploaded = models.DateTimeField(auto_now_add=True) #allows realtime accuracy upon upload

    #string representation of model
def _str_(self):
    return self.text
