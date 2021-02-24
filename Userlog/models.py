from django.db import models

# Create your models here.

#first create the class

class UserTopic(models.Model):
    #User interest
    text = models.CharField(max_length=120, null = True) #we want to display characters with max 250
    date_added = models.DateTimeField(auto_now_add=True) #allows realtime accuracy upon upload

    #string representation of model
    def __str__(self):
        return self.text


#entry model
class Entry(models.Model):
    topic = models.ForeignKey(UserTopic, on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50]+"..."

# ...
on_delete=models.DO_NOTHING,
# ...
    


