from django.shortcuts import render,HttpResponse,redirect

from app01 import models
def index(request):
    return  render(request, "index.html",)

def get_data(request):
    user_list = models.UserInfo.objects.all()
    return render(request,"tpl.html",{"user_list": user_list})
