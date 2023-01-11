from django.shortcuts import render
from .models import Group,Chat

# Create your views here.

def index(request,groupname):
  group = Group.objects.filter(name = groupname).first()
  chats=[]
  if group:
    chats = Chat.objects.filter(group=group)
  else:
    group = Group(name = groupname)
    group.save()
  return render(request,'index.html',{'groupname':groupname,'chats':chats})
