from django.shortcuts import render
from django.http import HttpResponse
from .models import UserTopic
from .models import Entry
from .models import *



# Create your views here.
def home(request):
    usertopics_objects = UserTopic.objects.all()
    entry_objects = Entry.objects.all()
    context = {
        'entry_objects': entry_objects,
        'usertopics_objects': usertopics_objects,      
    }
    return render(request, 'user_log/dashboard.html', context)

def customer_page(request, pk_test):
    customer_objects = customer.objects.get(id=pk_test)
    usertopics_objects = UserTopic.objects.all()
   # entry_objects = customer.entry_set.all()
    entry_objects = Entry.objects.all()
    context = {
        'entry_objects': entry_objects,
        'usertopics_objects': usertopics_objects,
        'customer_objects': customer_objects,      
    }
    
    return render(request, 'user_log/customer.html', context)

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
    posts = UserTopic.objects.all()
    topics = UserTopic.objects.order_by('date_added')
    context ={
        'topics': topics,
        'posts':posts
    }
    return render(request,'User_log/Userlogs.html',context)




#def posts(request):
 #   posts = UserTopic.objects.all()
  #  context = {'posts':posts}
   # return render(request,'user_log/Userlogs.html', context)
   

#create view for TopicForm

from .forms import TopicForm
#define below


#then crea new entry model forms