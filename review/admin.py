from django.contrib import admin

# Register your models here.
from .models import Profile, Course, Student, AssignmentGeneral, Assignment, Reviewer, Review, Upload, Notifications

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(AssignmentGeneral)
admin.site.register(Assignment)
admin.site.register(Reviewer)
admin.site.register(Review)
admin.site.register(Upload)
admin.site.register(Notifications)
