from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Length
# Create your views here.
def insert_topic(request):
    tn=input('enter topic name:')
    obj=Topic.objects.get_or_create(topic_name=tn)[0]
    obj.save()
    return HttpResponse('Topic data inserted succesfully')

def insert_webpage(request):
    tn=input('enter topic name:')
    url=input('enter url:')
    name=input('enter name :')
    obj=Topic.objects.get_or_create(topic_name=tn)[0]
    obj.save()
    w=Webpage.objects.get_or_create(topic_name=obj,name=name,url=url)[0]
    w.save()
    
    return HttpResponse('webpage data inserted succesfully ')

def insert_Accessrecords(request):
    tn=input('enter topic name:')
    url=input('enter url:')
    name=input('enter name :')
    date = input('enter date:')
    obj=Topic.objects.get_or_create(topic_name=tn)[0]
    obj.save()
    w=Webpage.objects.get_or_create(topic_name=obj,name=name,url=url)[0]
    w.save()
    Record = AccessRecord.objects.get_or_create(name=w,date = date)[0]
    Record.save()
    return HttpResponse('AccessRecord data inserted succesfully ')
    
def show_Topic_data(request):
    data = Topic.objects.all()
    d={'data':data}
    return render(request,'topic.html',context=d)
     
def show_webpage_data(request):
    data = Webpage.objects.all()
    data=Webpage.objects.order_by('name') # order_by 
    data=Webpage.objects.order_by('-name') # order_by in descending order
    data=Webpage.objects.filter(Q())
    d={'data':data}
    return render(request,'webpage.html',context=d)

def show_AccessRecord_data(request):
    data = AccessRecord.objects.all()
    d={'data':data}
    return render(request,'Access.html',context=d)

         
    


    
