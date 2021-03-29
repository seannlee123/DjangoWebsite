from django.shortcuts import render
from django.http import HttpResponse
from .models import UserTopic
from .models import Entry
from .models import Tag


# Create your views here.
def home(request):
    return render(request, 'user_log/dashboard.html')

def customer_page(request):
    return render(request, 'user_log/customer.html')

def welcome(request):
    return HttpResponse("welcome,  This is welcome")

def index(request):
    return render(request, 'user_log/navbar.html')
 #this is to direct to the templates

  #we need to bring our models

#I may need to make a view for entry by itself
def user_list_view(request):
   
    usertopics_objects = UserTopic.objects.all()
    entry_objects = Entry.objects.all()
    context = {
       
        'usertopics_objects': usertopics_objects,
        'entry_objects': entry_objects,
    }
    return render(request,'user_log/Userpost.html',context)
    #this is to direct to the templates

def topic_view(request):
    
    topics = UserTopic.objects.order_by('date_added')
    context ={
        'topics': topics,
    }
    return render(request,'User_log/Userlogs.html',context)