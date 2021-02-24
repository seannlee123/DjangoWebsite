from django.shortcuts import render
from django.http import HttpResponse

from .models import UserTopic
from .models import Entry

# Create your views here.
def home(request):
    return HttpResponse("This is test page")

def welcome(request):
    return HttpResponse("Hello welcome to the page")


def user_list_view(request):
    user_objects = UserTopic.objects.all()


    context = {
        'user_objects': user_objects
    }

    return render(request, "index.html", context)
