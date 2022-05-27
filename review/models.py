from turtle import title
from django.db import models
import uuid
from django.db.models.deletion import SET_NULL
from django.db.models.expressions import Value
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import BooleanField

# Create your models here.
class Profile(models.Model):
    USER_TYPE = (
                ('admin','Admin'),
                ('instructor','Instructor'),
                ('student','Student'),
        )
    username = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=50, choices= USER_TYPE)
    isapproved = BooleanField(required=True)
    userid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.user.email)

#@receiver(post_save, sender = Profiles)        
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def deleteUser(sender, instance, **kwargs): 
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender = User)
post_delete.connect(deleteUser, sender = Profile)


class Course(models.Model):
    courseid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    instructor = models.ForeignKey(Profile,  null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Student(models.Model):
    studentid = models.ForeignKey(Profile,  null=True, blank=True, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course,  null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.studentid.email)

class AssignmentGeneral(models.Model):
    courseid = models.ForeignKey(Course,  null=True, blank=True, on_delete=models.CASCADE)
    assid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    duedate = models.DateField(auto_now_add=False)
    duetime = models.TimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Assignment(models.Model):
    assignmentid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    assignee = models.ForeignKey(Profile,  null=True, blank=True, on_delete=models.CASCADE)
    group = models.IntegerField(default=0, null=True, blank=True)
    assgeneral = models.ForeignKey(AssignmentGeneral,  null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, default='a', upload_to='uploadFiles/')
    body = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.assignmentid)

class Reviewer(models.Model):
    reviewid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    reviewer = models.ForeignKey(Profile,  null=True, blank=True, on_delete=models.CASCADE)
    group = models.IntegerField(default=0, null=True, blank=True)
    assgeneral = models.ForeignKey(AssignmentGeneral,  null=True, blank=True, on_delete=models.CASCADE)
    #assigneeid = models.ForeignKey(Assignment,  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reviewer)

class Review(models.Model):
    reviewid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    assignmentid = models.ForeignKey(Assignment,  null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, upload_to='upload/reviewFiles/')
    body = models.TextField(max_length=3000)
    reviewerid = models.ForeignKey(Reviewer,  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reviewid)

class Upload(models.Model):
    uploadid = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    body = models.TextField(max_length=3000, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='uploadFiles/')
    assignmentid = models.ForeignKey(Assignment,  null=True, blank=True, on_delete=models.CASCADE)
    reviewid = models.ForeignKey(Review,  null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uploadid)