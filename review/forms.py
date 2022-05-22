from django import forms
import datetime as dt
from django.db.models import fields
from django.forms import ModelForm
from django.forms.fields import DateTimeField
from django.forms.widgets import DateInput, DateTimeInput, PasswordInput
from .models import Profile, Course, AssignmentGeneral, Assignment, Review, Reviewer, Upload, Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'instructor', ]

class AssignmentCreationForm(ModelForm):
    class Meta:
        model = AssignmentGeneral
        fields = [ 'courseid', 'title', 'description', 'duedate', 'duetime']

class ReviewCreationForm(ModelForm):
    class Meta:
        model = Reviewer
        fields = [ 'assgeneral', 'reviewer', 'group']

class AddtoCourse(ModelForm):
    class Meta:
        model = Student
        fields = ['studentid', 'courseid']

class AssignStudents(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignee', 'assgeneral', 'group']

class AssignmentUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['body', 'file']

class ReviewUploadForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'file']

class DefineUserType(ModelForm):
    class Meta:
        model = Profile
        fields = ['type']