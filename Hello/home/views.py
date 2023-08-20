from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from .models import *
from django.http import JsonResponse
from django.contrib import messages
import random
from rest_framework.views import APIView

def index(request):
    context = {
        "variable1":"QUIZ IS NICE!!",
        "variable2":"QUIZ IS FUN!!"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")
def contact(request):
    if request.method == "POST":
       
        username = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        
        if User.objects.filter(username=username).exists():  #to display a message 
                messages.info(request,'Username Taken ,please enter a different username ')
                return redirect('contact')
        
        contact = student(name=username, email=email, phone=phone, password=password, date = datetime.today())
        contact.save()

        myuser= User.objects.create_user(name1,email1,password1)
        myuser.save()
        messages.success(request, 'Your message has been sent and user is created!')

        
    return render(request, 'contact.html')

def feed(request):
    if request.method == "POST":
        feed= request.POST.get('feed')

        feed= feedback(feedback=feed)
        feed.save()
        messages.success(request, 'thankyou for the  feedback!')
    return redirect("/")

    

def loginUser(request):
    error_message = ''
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/quizpage")

        else:
           error_message = "Invalid login credentials. Please try again."
           context = {'error_message': error_message}
           return render(request, 'login.html', context)

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")



def quizpage(request):
    context = {'categories':quiz_topic.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'quizpage.html',context) 

def quiz(request):
    context={'category':request.GET.get('category')}

   
    return render(request,'quiz.html',context)

def Login(request):
    return render(request,'login.html')



def get_quiz(request):
    try:
        question_objs=questions.objects.all()
         
        if request.GET.get('category'):
            question_objs=question_objs.filter(qid__topic__icontains=request.GET.get('category'))

        question_objs=list(question_objs)
        data=[]
        random.shuffle(question_objs)

        for question_obj in question_objs:
           
            data.append({
                "qno":question_obj.qno,
                "topic":question_obj.qid.topic,
                "question":question_obj.question,
                "answers":question_obj.get_answers()
            })
        payload={'status':True,'data':data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")