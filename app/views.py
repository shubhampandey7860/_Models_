from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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
    data=Webpage.objects.order_by('topic_name')
    data=Webpage.objects.filter(Q(name__startswith='m')& Q(url__startswith='https'))
    # data=Webpage.objects.all()[:3]
   
    
    d={'data':data}
    return render(request,'webpage.html',context=d)

def show_AccessRecord_data(request):
    data = AccessRecord.objects.all()
    data = AccessRecord.objects.filter(date__day='07')
    data = AccessRecord.objects.filter(date__year__gt ='1985') # it will check which year is gt than
    d = {'data':data}
    return render(request,'Access.html',context=d)

def update_webpage_data(request):
    data=Webpage.objects.filter(name='Msdhoni').update(name='Virat Kohali')
    T=Topic.objects.get_or_create(topic_name='chess')[0]
    T.save()
    data=Webpage.objects.update_or_create(name='Major Dhyanchandra',defaults={'topic_name':T,'name':'Major Dhyanchandra','url':'http://majordhyanchandra.com'})
    data=Webpage.objects.all()
    d={'data':data}
    return render(request,'webpage.html',context=d)
     

         
    


    
