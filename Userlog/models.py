from django.db import models

# Create your models here.

#first create the class
#we need to make userclass

class customer(models.Model):
    name = models.CharField(max_length= 200, null = True)
    phone = models.CharField(max_length= 200, null = True)
    email = models.CharField(max_length= 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.name


class UserTopic(models.Model):
    #category for user to chose
    #User interest
    text = models.CharField(max_length=120, null =True) #we want to display characters with max 250
    date_added = models.DateTimeField(auto_now_add=True, null=True ) #allows realtime accuracy upon upload
    #string representation of model
    def __str__(self):
        return self.text


class Tag(models.Model):
    tag_name = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.tag_name
   
   
#entry model

class Entry(models.Model):
    cust_name = models.ForeignKey(customer, null= True, on_delete=models.SET_NULL)
    tags = models.ForeignKey(Tag, null = True, on_delete=models.CASCADE)
    topic = models.ForeignKey(UserTopic, null = True, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
 
class Meta:
    verbose_name_plural = 'entries'
    def __str__(self):
        return self.text[:50]+"..."
# ...
on_delete=models.DO_NOTHING,

        
       


     


