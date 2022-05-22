from cgi import print_form
from multiprocessing import context
import profile
from django.shortcuts import render
import datetime
from typing import Any
from django.core.files.base import ContentFile
from django.forms.widgets import HiddenInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Course, AssignmentGeneral, Assignment, Review, Upload
from .forms import UserCreationForm, CourseCreationForm, AssignmentCreationForm, AssignStudents, AssignmentUploadForm, ReviewUploadForm, DefineUserType, AddtoCourse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

# Create your views here.

def register(request):
    page='register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account is created! You need to get approval for the activation!')
            login(request, user)
            return redirect('courses')
            
        else:
            messages.success(request, 'An error has occurred during the registration!')

    context = {'page':page, 'form':form}
    return render(request, 'login_register.html', context)

def loginUser(request):
    page='login'

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        #try:
        #    user = User.objects.get(username)
        #except:
        #    messages.error(request, "User does not registered")

        user = authenticate(request, username=username, password=password)

        

        if user is not None:
            login(request, user)
            profile = request.user.profile
            if profile.type == 'admin':
                return redirect ('users')
            else:
                return redirect ('courses')
        else:
           messages.error(request,'username or password is incorrect')

        

        if request.user.is_authenticated:
            if profile.type == 'admin':
                return redirect ('users')
            else:
                return redirect ('courses')

    return render(request, 'login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, "User is succesfuly logged out")
    return redirect('login')

#@login_required(login_url="login")
def courses(request):
     return render(request, 'courses.html')

def users(request):
    page='users'
    profile = request.user.profile
    usersObj = Profile.objects.filter()
    form = DefineUserType()

    if profile.type == 'admin':
        if request.method == 'POST':
            form = DefineUserType(request.POST)
        if form.is_valid():
            form.save() 
    
    context = {'page':page, 'profile':profile, 'usersObj':usersObj}
    return render(request, 'users.html', context)

def approveUsers(request, pk):
    page='user'
    profile = request.user.profile
    userObj = Profile.objects.get(username=pk)
    print(userObj)
    form = DefineUserType(instance = userObj)

    if profile.type == 'admin':
        if request.method == 'POST':
            form = DefineUserType(request.POST, instance = userObj)
        if form.is_valid():
            form.save() 
    
    context = {'page':page, 'profile':profile, 'userObj':userObj}
    return render(request, 'user.html', context)

def createCourse(request):
    profile = request.user.profile
    form = CourseCreationForm()
    instructorsList = Profile.objects.filter(type='instructor')

    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
    if form.is_valid():
        form.save() 
    
    context = {'form':form, 'profile':profile, 'instructorsList':instructorsList}
    return render(request, 'createcourse.html', context)

def createAssignment(request):
    profile = request.user.profile
    form = AssignmentCreationForm()
    coursesList = Course.objects.filter()

    if request.method == 'POST':
        form = AssignmentCreationForm(request.POST)
        print(form.data)
    if form.is_valid():
        form.save() 
    
    context = {'form':form, 'profile':profile, 'coursesList':coursesList}
    return render(request, 'createassignment.html', context)

def assignStudents(request):
    profile = request.user.profile
    form = AssignStudents()
    assignmentList = AssignmentGeneral.objects.filter()
    studentList = Profile.objects.filter(type='student')

    if request.method == 'POST':
        form = AssignStudents(request.POST)
        print(form.data)
    if form.is_valid():
        form.save() 
    
    context = {'form':form, 'profile':profile, 'assignmentList':assignmentList, 'studentList':studentList}
    return render(request, 'assignstudents.html', context)

def addtoCourse(request):
    profile = request.user.profile
    form = AddtoCourse()
    courseList = Course.objects.filter()
    studentList = Profile.objects.filter(type='student')

    if request.method == 'POST':
        form = AddtoCourse(request.POST)
        print(form.data)
    if form.is_valid():
        form.save() 
    
    context = {'form':form, 'profile':profile, 'courseList':courseList, 'studentList':studentList}
    return render(request, 'addtocourse.html', context)



