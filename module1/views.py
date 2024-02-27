import pytz
from django.shortcuts import render
from django.http import HttpResponse
import random
import string

#here logic and functions are written
# Create your views here.
def hello(request):
    return render(request,'hello123.html')#after creating a function u should write the paht in urls.py in add(module1)
def hello1(request):
    return HttpResponse("<center><font color=blue>welcome to TTm Page</font></center>")#return statement is mandetary
def homepage(request):
    return render(request,'homepage.html')#after creating a function u have to add the path of that fun in urls
def travelpackage(request):
    return render(request,'travelpackage.html')
def print1(request):
    return render(request,'printtoconsole.html')#this is used to call the html file
def printtoconsole(request):
    if request.method=="POST":
        user_input=request.POST['hema']
        print(f'USER INPUT:{user_input}')
    #return HttpResponse('form submitted successfully')
        a1={'user_input':user_input}
    return render(request,'printtoconsole.html',a1)
def ran(request):
    return render(request,'random123.html')
def random123(request):
    if request.method == 'POST':
        input1=request.POST['input1']
        input2=int(input1)
        result_str=''.join(random.sample(string.digits,input2))
        print(result_str)
        context={'result_str':result_str}
    return render(request,"random123.html",context)



def getdate1(request):
    return render(request,'get_date.html')
from .forms import *
import datetime
from django.shortcuts import render

def get_date(request):
    if request.method == 'POST':
        form = Integerdateform(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = Integerdateform()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request, 'pytexample.html')
def tzfunctionlogic(request):
    list1=[]
    if request.method=='POST':
        input1=request.POST['input1']
        time1=pytz.timezone(input1)
    context={'time1':time1}
    return render(request,"pytz")


def reg(request):
    return render(request, 'database.html')


from .models import *
from django.shortcuts import render, redirect


def registerloginfunction(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            msg1 = "Email already exists.Choose different one."
            return render(request, 'database.html', {'msg1': msg1})
        Register.objects.create(name=name, email=email, password=password, phonenumber=phonenumber)
        return redirect('homepage')
    return render(request, 'database.html')



import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def fam(request):
    return render(request,'famous_destinations.html')

import requests
def weatherpagecall(request):
    return render(request,'weatherpage.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '63b5c7db0b9c3da271ed2ae14dc60501'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherpage.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherpage.html', {'error_message': error_message})

from django.contrib import messages
from django.contrib.auth.models import  User, auth
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.post['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'homepage.html')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'opps! username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully')
                return render(request,'login.html')
        else:
            messages.info(request,'password do not match')
            return render(request,'signup.html')






