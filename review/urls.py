    
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
    path('assignment/<str:pk>/assignstudents', views.assignStudents, name="assignstudents"),
    path('assignment/<str:pk>/createreview', views.createReview, name="assignreviewers"),
    path('assignreviewers/<str:pk>/', views.assignReviewers, name="assignreviewers"),
    path('addtocourse/', views.addtoCourse, name="addtoCourse"),
    path('assignments/<str:pk>/', views.assignments, name="assignments"),
    path('assignment/<str:pk>/', views.assignment, name="assignment"),
    path('assignment/<str:pk>/upload', views.uploadAssignment, name="uploadassignment"),
    path('reviews/<str:pk>/', views.reviews, name="reviews"),
    path('review/<str:pk>/', views.review, name="review"),

]