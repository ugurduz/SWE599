    
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
    
urlpatterns =[    
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('', views.courses, name="courses"),
    path('users', views.users, name="users"),
    path('user/<str:pk>/', views.approveUsers, name="user"),
    path('createcourse/', views.createCourse, name="createcourse"),
    path('createassignment/', views.createAssignment, name="createassignment"),
    path('assignstudents/', views.assignStudents, name="assignstudents"),
    path('createreview/', views.createReview, name="createreview"),
    path('assignreviewers/', views.assignReviewers, name="assignreviewers"),
    path('addtocourse/', views.addtoCourse, name="addtoCourse"),
    path('assignments/', views.assignments, name="assignments"),
    path('assignment/<str:pk>/', views.assignment, name="assignment"),
    path('reviews/', views.reviews, name="reviews"),
    path('review/<str:pk>/', views.review, name="review"),

]