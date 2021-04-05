from django import forms

from .models import UserTopic, Entry


#465
#this will allow us to create a based page for
#  user to input or create a new one
class TopicForm(forms.ModelForm):
     class Meta:
        model = UserTopic
        fields = ['text']
        labels = {'text': ''}

#this is for adding new entries 
class EntryForm(forms.ModelForm):
     class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}