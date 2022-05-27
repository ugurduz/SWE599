from cgi import print_form
from collections import UserList
from multiprocessing import context
import profile
from django.shortcuts import render
import datetime
from typing import Any
from django.core.files.base import ContentFile
from django.forms.widgets import HiddenInput
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Course, AssignmentGeneral, Assignment, Review, Upload, Student, Reviewer
from .forms import UserCreationForm, CourseCreationForm, AssignmentCreationForm, ReviewCreationForm, AssignStudents,AssignReviewers, AssignmentUploadForm, ReviewUploadForm, DefineUserType, AddtoCourse
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
    page = 'courses'
    profile = request.user.profile
    studentObj = Student.objects.filter(studentid = profile.userid)
    InstructorObj = Profile.objects.filter(userid = profile.userid)
    coursesObj = Course.objects.filter(instructor=profile)

    context = {'page':page,'profile':profile, 'studentObj':studentObj, 'instructorObj':InstructorObj, 'coursesObj':coursesObj}

    return render(request, 'courses.html', context)

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

def assignStudents(request, pk):
    profile = request.user.profile
    form = AssignStudents()
    assignmentList = AssignmentGeneral.objects.get(assid=pk)
    print(assignmentList.assid)
    courseid = assignmentList.courseid
    studentList = Student.objects.filter(courseid = courseid)

    if request.method == 'POST':
        form = AssignStudents(request.POST)

        if form.is_valid():
            print(form.data)
            form.save() 
    
    context = {'form':form, 'profile':profile, 'assignmentList':assignmentList, 'studentList':studentList, 'courseid':courseid}
    return render(request, 'assignstudents.html', context)

def createReview(request, pk):
    profile = request.user.profile
    form = ReviewCreationForm()
    usersList = Profile.objects.filter(type='student')
    assignmentsList = AssignmentGeneral.objects.get(assid = pk)
    coursesList = Course.objects.filter(instructor = profile)
    courseid2 = assignmentsList.courseid
    
    studentList = Student.objects.filter(courseid = courseid2)
    print(studentList)

    if request.method == 'POST':
        form = ReviewCreationForm(request.POST)
        print(form.data)
    if form.is_valid():
        print(form.data)
        form.save() 
    
    context = {'form':form, 'profile':profile, 'coursesList':coursesList, 'assignmentsList':assignmentsList, 'usersList':usersList, 'studentList':studentList}
    return render(request, 'assignreviewers.html', context)

def assignment(request, pk):
    page = 'assignment'
    profile = request.user.profile
    assignmentObj = Assignment.objects.get(assignmentid = pk)
    print(assignmentObj)
    #assignments = AssignmentGeneral.objects.get(assid = pk)
    date = datetime.date.today()
    print(date)
    print(assignmentObj.assgeneral.duedate)
    form = AssignStudents(instance = assignmentObj)
    context = {'page':page,'profile':profile, 'assignmentObj':assignmentObj, 'form':form, 'date':date}   

    return render(request, 'assignment.html', context)


def assignReviewers(request, pk):
    profile = request.user.profile
    form = AssignReviewers()
    assignmentList = AssignmentGeneral.objects.filter(assid=pk)
    studentList = Profile.objects.filter(type='student')

    if request.method == 'POST':
        form = AssignReviewers(request.POST)
        
    if form.is_valid():
        print(form.data)
        form.save() 
    
    context = {'form':form, 'profile':profile, 'assignmentList':assignmentList, 'studentList':studentList}
    return render(request, 'assignreviewers.html', context)

def assignments(request,pk):
    page = 'assignments'
    profile = request.user.profile
    assignmentsObj = Assignment.objects.filter(assignee=profile)
    instructorass = Assignment.objects.filter()
    assignments = AssignmentGeneral.objects.filter(courseid=pk)
    studentObj = Student.objects.filter(studentid = profile.userid)
    InstructorObj = Profile.objects.filter(userid = profile.userid)
    studentList = Student.objects.filter(courseid = pk)
    context = {'page':page,'profile':profile, 'studentObj':studentObj, 'assignmentsObj':assignmentsObj, 'instructorObj':InstructorObj, 'assignments':assignments, 'instructorass':instructorass, 'studentList':studentList}
    return render(request, 'assignments.html', context)

def uploadAssignment(request, pk):
    page = 'uploadassignment'
    profile = request.user.profile
    assignmentObj = Assignment.objects.get(assignmentid = pk)
    form = AssignmentUploadForm(instance=assignmentObj)

    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST, request.FILES, instance=assignmentObj)
        print(form.data)
    if form.is_valid():
        if len(request.FILES) != 0:
                form.file = request.FILES['file']
        form.save() 

    context = {'page':page,'profile':profile, 'assignmentsObj':assignmentObj, 'form':form}
    return render(request, 'uploadassignment.html', context)

def uploadReview(request, pk):
    page = 'uploadreview'
    profile = request.user.profile
    reviewObj = Reviewer.objects.get(assgeneral = pk)
    group = reviewObj.group
    form = ReviewUploadForm(instance=reviewObj)
    assignmentsObj = Assignment.objects.filter(assgeneral = pk, group = group)

    if request.method == 'POST':
        form = ReviewUploadForm(request.POST, request.FILES, instance=reviewObj)
        print(form.data)
    if form.is_valid():
        if len(request.FILES) != 0:
                form.file = request.FILES['file']
        for assignment in assignmentsObj:
            Review.objects.create(assignmentid = assignment, reviewerid = reviewObj)

        form.save() 

    context = {'page':page,'profile':profile, 'assignmentsObj':reviewObj, 'form':form}
    return render(request, 'uploadreview.html', context)


def review(request):

    return render(request, 'review.html', context)

def reviews(request, pk):
    page = 'reviews'
    profile = request.user.profile
    reviewList = Reviewer.objects.filter(reviewer=profile)
    assignmentGenerals = AssignmentGeneral.objects.filter(courseid=pk)
    assignments = Assignment.objects.filter()
    studentList = Student.objects.filter(courseid = pk)

    context = {'page':page,'profile':profile, 'reviewList':reviewList, 'assignmentGenerals':assignmentGenerals, 'assignments':assignments, 'studentList':studentList}
    return render(request, 'reviews.html', context)

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



