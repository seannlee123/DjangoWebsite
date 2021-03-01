from django.shortcuts import render
from django.http import HttpResponse

from .models import UserTopic
from .models import Entry

# Create your views here.
def home(request):
    return HttpResponse("This is home page")

def welcome(request):
    return HttpResponse("welcome,  This is welcome")

def index(request):
    return render(request, 'user_log/index.html')




"""
#from book
def index(request):
    user_objects = UserTopic.objects.all()
    entry_objects1 = Entry.objects.all()
    context = {
        'user_objects': user_objects,
        'entry_objects1':entry_objects1,
    }
    #homepage for userlog
    return render(request, 'Userlog/index.html', context)

"""
from . models import UserTopic,Entry #we need to bring our models

def user_list_view(request):
    usertopics_objects = UserTopic.objects.all()
    entry_objects = Entry.objects.all()
    context = {
        'user_objects': usertopics_objects,
        'entry_objects': entry_objects,
    }

    return render(request,'user_log/models.html',context)
