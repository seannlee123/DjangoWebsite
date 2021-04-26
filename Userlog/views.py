from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import UserTopic
from .models import Entry
from .models import *
from .forms import TopicForm, EntryForm



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
    entry_objects = customer_objects.entries.all()
    context = {
        'entry_objects': entry_objects,
        'customer_objects': customer_objects,
    }

    return render(request, 'user_log/customer.html',context)



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


def createNew_post(request):
    topic_form = TopicForm()
    if request.method == "POST":
        #print('Printing POST:',request.POST)
         topic_form = TopicForm(request.POST)
         if  topic_form.is_valid():
             topic_form.save()
             return redirect('/')


    entry_form = EntryForm()
    if request.method == "POST":
        #print('Printing POST:',request.POST)
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('/')
    context ={
        'topic_form':topic_form,
        'entry_form':entry_form
    }

    return render(request, 'user_log/new_post.html', context)

#return to 11:16 CRUD pt 10

def update_post(request, pk):
    entry = Entry.objects.get(id=pk)
    entry_form = EntryForm(instance=entry)
    if request.method == "POST":
            #print('Printing POST:',request.POST)
        entry_form = EntryForm(request.POST,instance=entry )
        if entry_form.is_valid():
            entry_form.save()
            return redirect('/')
    context ={
        'entry_form':entry_form
    }

    return render(request, 'user_log/new_post.html', context)

def delete_post(request, pk):
    entry = Entry.objects.get(id=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('/')
    context ={
        'item':entry

    }
    return render(request, 'user_log/delete_post.html', context)


